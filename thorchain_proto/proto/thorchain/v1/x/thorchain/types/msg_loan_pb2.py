# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_loan.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-thorchain/v1/x/thorchain/types/msg_loan.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a\x14gogoproto/gogo.proto\"\xea\x05\n\x0bMsgLoanOpen\x12?\n\x05owner\x18\x01 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12-\n\x10\x63ollateral_asset\x18\x02 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12J\n\x11\x63ollateral_amount\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12H\n\x0etarget_address\x18\x04 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12)\n\x0ctarget_asset\x18\x05 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12@\n\x07min_out\x18\x06 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12K\n\x11\x61\x66\x66iliate_address\x18\x07 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12O\n\x16\x61\x66\x66iliate_basis_points\x18\x08 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x12\n\naggregator\x18\t \x01(\t\x12!\n\x19\x61ggregator_target_address\x18\n \x01(\t\x12P\n\x17\x61ggregator_target_limit\x18\x0b \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x41\n\x06signer\x18\x0c \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\"\xa9\x02\n\x10MsgLoanRepayment\x12?\n\x05owner\x18\x01 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12-\n\x10\x63ollateral_asset\x18\x02 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12 \n\x04\x63oin\x18\x03 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12@\n\x07min_out\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x41\n\x06signer\x18\x05 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_loan_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGLOANOPEN.fields_by_name['owner']._options = None
  _MSGLOANOPEN.fields_by_name['owner']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _MSGLOANOPEN.fields_by_name['collateral_asset']._options = None
  _MSGLOANOPEN.fields_by_name['collateral_asset']._serialized_options = b'\310\336\037\000'
  _MSGLOANOPEN.fields_by_name['collateral_amount']._options = None
  _MSGLOANOPEN.fields_by_name['collateral_amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _MSGLOANOPEN.fields_by_name['target_address']._options = None
  _MSGLOANOPEN.fields_by_name['target_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _MSGLOANOPEN.fields_by_name['target_asset']._options = None
  _MSGLOANOPEN.fields_by_name['target_asset']._serialized_options = b'\310\336\037\000'
  _MSGLOANOPEN.fields_by_name['min_out']._options = None
  _MSGLOANOPEN.fields_by_name['min_out']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _MSGLOANOPEN.fields_by_name['affiliate_address']._options = None
  _MSGLOANOPEN.fields_by_name['affiliate_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _MSGLOANOPEN.fields_by_name['affiliate_basis_points']._options = None
  _MSGLOANOPEN.fields_by_name['affiliate_basis_points']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _MSGLOANOPEN.fields_by_name['aggregator_target_limit']._options = None
  _MSGLOANOPEN.fields_by_name['aggregator_target_limit']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _MSGLOANOPEN.fields_by_name['signer']._options = None
  _MSGLOANOPEN.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGLOANREPAYMENT.fields_by_name['owner']._options = None
  _MSGLOANREPAYMENT.fields_by_name['owner']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _MSGLOANREPAYMENT.fields_by_name['collateral_asset']._options = None
  _MSGLOANREPAYMENT.fields_by_name['collateral_asset']._serialized_options = b'\310\336\037\000'
  _MSGLOANREPAYMENT.fields_by_name['coin']._options = None
  _MSGLOANREPAYMENT.fields_by_name['coin']._serialized_options = b'\310\336\037\000'
  _MSGLOANREPAYMENT.fields_by_name['min_out']._options = None
  _MSGLOANREPAYMENT.fields_by_name['min_out']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _MSGLOANREPAYMENT.fields_by_name['signer']._options = None
  _MSGLOANREPAYMENT.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGLOANOPEN._serialized_start=113
  _MSGLOANOPEN._serialized_end=859
  _MSGLOANREPAYMENT._serialized_start=862
  _MSGLOANREPAYMENT._serialized_end=1159
# @@protoc_insertion_point(module_scope)
