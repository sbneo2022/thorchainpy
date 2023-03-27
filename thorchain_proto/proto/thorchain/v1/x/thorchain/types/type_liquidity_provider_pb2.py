# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/type_liquidity_provider.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<thorchain/v1/x/thorchain/types/type_liquidity_provider.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a\x14gogoproto/gogo.proto\"\xbe\x05\n\x11LiquidityProvider\x12\"\n\x05\x61sset\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x46\n\x0crune_address\x18\x02 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12G\n\rasset_address\x18\x03 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12\x17\n\x0flast_add_height\x18\x04 \x01(\x03\x12\x1c\n\x14last_withdraw_height\x18\x05 \x01(\x03\x12>\n\x05units\x18\x06 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x45\n\x0cpending_rune\x18\x07 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x46\n\rpending_asset\x18\x08 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12S\n\rpending_tx_Id\x18\t \x01(\tB<\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x0bPendingTxID\x12K\n\x12rune_deposit_value\x18\n \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12L\n\x13\x61sset_deposit_value\x18\x0b \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x42\x31Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.type_liquidity_provider_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _LIQUIDITYPROVIDER.fields_by_name['asset']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['asset']._serialized_options = b'\310\336\037\000'
  _LIQUIDITYPROVIDER.fields_by_name['rune_address']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['rune_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _LIQUIDITYPROVIDER.fields_by_name['asset_address']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['asset_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _LIQUIDITYPROVIDER.fields_by_name['units']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['units']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _LIQUIDITYPROVIDER.fields_by_name['pending_rune']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['pending_rune']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _LIQUIDITYPROVIDER.fields_by_name['pending_asset']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['pending_asset']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _LIQUIDITYPROVIDER.fields_by_name['pending_tx_Id']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['pending_tx_Id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\013PendingTxID'
  _LIQUIDITYPROVIDER.fields_by_name['rune_deposit_value']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['rune_deposit_value']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _LIQUIDITYPROVIDER.fields_by_name['asset_deposit_value']._options = None
  _LIQUIDITYPROVIDER.fields_by_name['asset_deposit_value']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _LIQUIDITYPROVIDER._serialized_start=128
  _LIQUIDITYPROVIDER._serialized_end=830
# @@protoc_insertion_point(module_scope)
