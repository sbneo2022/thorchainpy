# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/type_ban_voter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3thorchain/v1/x/thorchain/types/type_ban_voter.proto\x12\x05types\x1a\x14gogoproto/gogo.proto\"z\n\x08\x42\x61nVoter\x12G\n\x0cnode_address\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x03\x12\x0f\n\x07signers\x18\x03 \x03(\tB=Z/gitlab.com/thorchain/thornode/x/thorchain/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00\xc8\xe1\x1e\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.type_ban_voter_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types\330\341\036\000\200\342\036\000\310\341\036\000'
  _BANVOTER.fields_by_name['node_address']._options = None
  _BANVOTER.fields_by_name['node_address']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _BANVOTER._serialized_start=84
  _BANVOTER._serialized_end=206
# @@protoc_insertion_point(module_scope)
