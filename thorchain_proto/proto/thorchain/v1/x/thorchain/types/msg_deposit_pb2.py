# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_deposit.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0thorchain/v1/x/thorchain/types/msg_deposit.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a\x14gogoproto/gogo.proto\"\xae\x01\n\nMsgDeposit\x12O\n\x05\x63oins\x18\x01 \x03(\x0b\x32\x0c.common.CoinB2\xaa\xdf\x1f*gitlab.com/thorchain/thornode/common.Coins\xc8\xde\x1f\x00\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x41\n\x06signer\x18\x03 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_deposit_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGDEPOSIT.fields_by_name['coins']._options = None
  _MSGDEPOSIT.fields_by_name['coins']._serialized_options = b'\252\337\037*gitlab.com/thorchain/thornode/common.Coins\310\336\037\000'
  _MSGDEPOSIT.fields_by_name['signer']._options = None
  _MSGDEPOSIT.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGDEPOSIT._serialized_start=116
  _MSGDEPOSIT._serialized_end=290
# @@protoc_insertion_point(module_scope)
