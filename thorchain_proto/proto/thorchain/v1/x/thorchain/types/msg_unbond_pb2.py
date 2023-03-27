# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_unbond.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/thorchain/v1/x/thorchain/types/msg_unbond.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a\x14gogoproto/gogo.proto\"\x93\x03\n\tMsgUnBond\x12\x1f\n\x05tx_in\x18\x01 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\x12G\n\x0cnode_address\x18\x02 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x46\n\x0c\x62ond_address\x18\x05 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12?\n\x06\x61mount\x18\x06 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x41\n\x06signer\x18\x07 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12P\n\x15\x62ond_provider_address\x18\x08 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_unbond_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGUNBOND.fields_by_name['tx_in']._options = None
  _MSGUNBOND.fields_by_name['tx_in']._serialized_options = b'\310\336\037\000'
  _MSGUNBOND.fields_by_name['node_address']._options = None
  _MSGUNBOND.fields_by_name['node_address']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGUNBOND.fields_by_name['bond_address']._options = None
  _MSGUNBOND.fields_by_name['bond_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _MSGUNBOND.fields_by_name['amount']._options = None
  _MSGUNBOND.fields_by_name['amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _MSGUNBOND.fields_by_name['signer']._options = None
  _MSGUNBOND.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGUNBOND.fields_by_name['bond_provider_address']._options = None
  _MSGUNBOND.fields_by_name['bond_provider_address']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGUNBOND._serialized_start=115
  _MSGUNBOND._serialized_end=518
# @@protoc_insertion_point(module_scope)