# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_noop.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.x.thorchain.types import type_observed_tx_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__observed__tx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-thorchain/v1/x/thorchain/types/msg_noop.proto\x12\x05types\x1a\x35thorchain/v1/x/thorchain/types/type_observed_tx.proto\x1a\x14gogoproto/gogo.proto\"\x8a\x01\n\x07MsgNoOp\x12,\n\x0bobserved_tx\x18\x01 \x01(\x0b\x32\x11.types.ObservedTxB\x04\xc8\xde\x1f\x00\x12\x41\n\x06signer\x18\x02 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\tB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_noop_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGNOOP.fields_by_name['observed_tx']._options = None
  _MSGNOOP.fields_by_name['observed_tx']._serialized_options = b'\310\336\037\000'
  _MSGNOOP.fields_by_name['signer']._options = None
  _MSGNOOP.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGNOOP._serialized_start=134
  _MSGNOOP._serialized_end=272
# @@protoc_insertion_point(module_scope)
