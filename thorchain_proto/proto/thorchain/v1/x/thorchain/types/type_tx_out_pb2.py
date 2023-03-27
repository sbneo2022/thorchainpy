# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/type_tx_out.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0thorchain/v1/x/thorchain/types/type_tx_out.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a\x14gogoproto/gogo.proto\"\x92\x05\n\tTxOutItem\x12=\n\x05\x63hain\x18\x01 \x01(\tB.\xfa\xde\x1f*gitlab.com/thorchain/thornode/common.Chain\x12\x44\n\nto_address\x18\x02 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12\x46\n\rvault_pub_key\x18\x03 \x01(\tB/\xfa\xde\x1f+gitlab.com/thorchain/thornode/common.PubKey\x12 \n\x04\x63oin\x18\x04 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12O\n\x07max_gas\x18\x06 \x03(\x0b\x32\x0c.common.CoinB0\xaa\xdf\x1f(gitlab.com/thorchain/thornode/common.Gas\xc8\xde\x1f\x00\x12\x10\n\x08gas_rate\x18\x07 \x01(\x03\x12>\n\x07in_hash\x18\x08 \x01(\tB-\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\x12?\n\x08out_hash\x18\t \x01(\tB-\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\x12\x1d\n\x0bmodule_name\x18\n \x01(\tB\x05\xea\xde\x1f\x01-R\x01-\x12\x12\n\naggregator\x18\x0b \x01(\t\x12\x1f\n\x17\x61ggregator_target_asset\x18\x0c \x01(\t\x12P\n\x17\x61ggregator_target_limit\x18\r \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x01\"G\n\x05TxOut\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12(\n\x08tx_array\x18\x02 \x03(\x0b\x32\x10.types.TxOutItemB\x04\xc8\xde\x1f\x00:\x04\x80\xdc \x01\x42=Z/gitlab.com/thorchain/thornode/x/thorchain/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00\xc8\xe1\x1e\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.type_tx_out_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types\330\341\036\000\200\342\036\000\310\341\036\000'
  _TXOUTITEM.fields_by_name['chain']._options = None
  _TXOUTITEM.fields_by_name['chain']._serialized_options = b'\372\336\037*gitlab.com/thorchain/thornode/common.Chain'
  _TXOUTITEM.fields_by_name['to_address']._options = None
  _TXOUTITEM.fields_by_name['to_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _TXOUTITEM.fields_by_name['vault_pub_key']._options = None
  _TXOUTITEM.fields_by_name['vault_pub_key']._serialized_options = b'\372\336\037+gitlab.com/thorchain/thornode/common.PubKey'
  _TXOUTITEM.fields_by_name['coin']._options = None
  _TXOUTITEM.fields_by_name['coin']._serialized_options = b'\310\336\037\000'
  _TXOUTITEM.fields_by_name['max_gas']._options = None
  _TXOUTITEM.fields_by_name['max_gas']._serialized_options = b'\252\337\037(gitlab.com/thorchain/thornode/common.Gas\310\336\037\000'
  _TXOUTITEM.fields_by_name['in_hash']._options = None
  _TXOUTITEM.fields_by_name['in_hash']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID'
  _TXOUTITEM.fields_by_name['out_hash']._options = None
  _TXOUTITEM.fields_by_name['out_hash']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID'
  _TXOUTITEM.fields_by_name['module_name']._options = None
  _TXOUTITEM.fields_by_name['module_name']._serialized_options = b'\352\336\037\001-'
  _TXOUTITEM.fields_by_name['aggregator_target_limit']._options = None
  _TXOUTITEM.fields_by_name['aggregator_target_limit']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\001'
  _TXOUT.fields_by_name['tx_array']._options = None
  _TXOUT.fields_by_name['tx_array']._serialized_options = b'\310\336\037\000'
  _TXOUT._options = None
  _TXOUT._serialized_options = b'\200\334 \001'
  _TXOUTITEM._serialized_start=116
  _TXOUTITEM._serialized_end=774
  _TXOUT._serialized_start=776
  _TXOUT._serialized_end=847
# @@protoc_insertion_point(module_scope)