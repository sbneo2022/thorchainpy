# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_network_fee.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4thorchain/v1/x/thorchain/types/msg_network_fee.proto\x12\x05types\x1a\x14gogoproto/gogo.proto\"\xdf\x01\n\rMsgNetworkFee\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x03\x12=\n\x05\x63hain\x18\x02 \x01(\tB.\xfa\xde\x1f*gitlab.com/thorchain/thornode/common.Chain\x12\x18\n\x10transaction_size\x18\x03 \x01(\x04\x12\x1c\n\x14transaction_fee_rate\x18\x04 \x01(\x04\x12\x41\n\x06signer\x18\x05 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_network_fee_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGNETWORKFEE.fields_by_name['chain']._options = None
  _MSGNETWORKFEE.fields_by_name['chain']._serialized_options = b'\372\336\037*gitlab.com/thorchain/thornode/common.Chain'
  _MSGNETWORKFEE.fields_by_name['signer']._options = None
  _MSGNETWORKFEE.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGNETWORKFEE._serialized_start=86
  _MSGNETWORKFEE._serialized_end=309
# @@protoc_insertion_point(module_scope)