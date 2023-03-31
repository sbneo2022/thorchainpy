#!/usr/bin/env bash

set -e pipefail

clean() {
  rm -rf ./thornode/ ./thorchainpy/ ./thornode-api-client/
}

gen_openapi_client() {
  git clone https://gitlab.com/thorchain/thornode.git

  openapi-python-client generate --path thornode/openapi/openapi.yaml

  rm -rf thorchain_api_client
  mv ./thornode-api-client/thornode_api_client/ ./thorchainpy/
}

# ------------------------------------------------
# SCRIPT STARTS HERE
# ------------------------------------------------

clean

gen_openapi_client

rm -rf thornode/ thornode-api-client/
