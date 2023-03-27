#!/usr/bin/env bash

set -e pipefail

# ------------------------------------------------ CONFIG
PKG_PATH="thorchain_proto"
PKG_PROTO_SUBDIR="$PKG_PATH/proto"
cosmos_sdk_version=v0.45.12
thorchain_version=v1.107.0
# ------------------------------------------------

# Add PKG_PATH as dir if it doesn't exist.
clean() {
  rm -rf ./proto/
  rm -rf ./thornode/
  rm -rf $PKG_PATH
  mkdir $PKG_PATH
}

copy_thorchain_protobuf_from_remote() {
  git clone --depth 1 --branch $thorchain_version https://gitlab.com/thorchain/thornode.git
  cp -r ./thornode/proto/ ./proto/
  cp ./thornode/go.mod go.mod
  cp ./thornode/go.sum go.sum
}

protoc_gen_gocosmos() {
  if ! grep "github.com/gogo/protobuf => github.com/regen-network/protobuf" go.mod &>/dev/null; then
    echo -e "\tPlease run this command from somewhere inside the thorchain folder."
    return 1
  fi

  # get protoc gocosmos plugin
  go get github.com/regen-network/cosmos-proto/protoc-gen-gocosmos@latest 2>/dev/null

  # get cosmos sdk from github
  go get github.com/cosmos/cosmos-sdk@$cosmos_sdk_version 2>/dev/null
}

code_gen() {
  echo "grabbing cosmos-sdk proto file locations from disk"
  echo "current dir: $(pwd)"

  cd ./thornode
  protoc_gen_gocosmos
  cosmos_sdk_dir=$(go list -f '{{ .Dir }}' -m github.com/cosmos/cosmos-sdk)
  cd -

  echo "grab all of the proto directories"
  echo "current dir: $(pwd)"
  proto_dirs=$(find $cosmos_sdk_dir/proto $cosmos_sdk_dir/third_party/proto ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
  echo "Proto Directories: "
  echo $proto_dirs

  # generate the protos for each directory
  for dir in $proto_dirs; do
    string=$dir
    prefix=$HOME/go/pkg/mod/github.com/
    prefix_removed_string=${string/#$prefix/}
    echo "------------ generating $prefix_removed_string ------------"
    # echo "$cosmos_sdk_dir"
    mkdir -p ./$PKG_PATH/${dir}
    python -m grpc_tools.protoc \
      -I proto \
      -I "$cosmos_sdk_dir/third_party/proto" \
      -I "$cosmos_sdk_dir/proto" \
      --python_out=$PKG_PROTO_SUBDIR \
      --grpc_python_out=$PKG_PROTO_SUBDIR \
      --mypy_out=$PKG_PROTO_SUBDIR \
      --mypy_grpc_out=$PKG_PROTO_SUBDIR \
      $(find "${dir}" -type f -name '*.proto')
  done

}

fix_google_apis() {
  mv $PKG_PROTO_SUBDIR/google $PKG_PROTO_SUBDIR/google_apis

  find . -type f -name '*.py' -exec sed -i 's/from google\.api/from google_apis\.api/g' {} +
}

# ------------------------------------------------
# __main__ : Start of script execution
# ------------------------------------------------

clean

copy_thorchain_protobuf_from_remote

code_gen

printf "import os\nimport sys\n\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" >$PKG_PROTO_SUBDIR/__init__.py

fix_google_apis

echo "Complete - generated Python types from proto"
# cleanup
rm go.mod go.sum
rm -rf thornode/ proto/

poetry run python scripts/init-py.py
echo "Complete - converted types directories into packages"
