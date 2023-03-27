# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/type_events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from thorchain.v1.x.thorchain.types import type_pool_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__pool__pb2
from thorchain.v1.x.thorchain.types import type_reserve_contributor_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__reserve__contributor__pb2
from thorchain.v1.x.thorchain.types import type_tx_out_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__tx__out__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0thorchain/v1/x/thorchain/types/type_events.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a.thorchain/v1/x/thorchain/types/type_pool.proto\x1a=thorchain/v1/x/thorchain/types/type_reserve_contributor.proto\x1a\x30thorchain/v1/x/thorchain/types/type_tx_out.proto\x1a\x14gogoproto/gogo.proto\"\xd9\x01\n\x07PoolMod\x12\"\n\x05\x61sset\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x41\n\x08rune_amt\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x10\n\x08rune_add\x18\x03 \x01(\x08\x12\x42\n\tasset_amt\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x11\n\tasset_add\x18\x05 \x01(\x08\"\x9f\x01\n\x0f\x45ventLimitOrder\x12\"\n\x06source\x18\x01 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12\"\n\x06target\x18\x02 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12\x44\n\x05tx_id\x18\x03 \x01(\tB5\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x04TxID\"\x82\x04\n\tEventSwap\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x44\n\x0bswap_target\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x42\n\tswap_slip\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x46\n\rliquidity_fee\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12N\n\x15liquidity_fee_in_rune\x18\x05 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x1f\n\x05in_tx\x18\x06 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\x12!\n\x07out_txs\x18\x07 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\x12&\n\nemit_asset\x18\x08 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12\x44\n\x0bsynth_units\x18\t \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"\xbd\x04\n\x11\x45ventAddLiquidity\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12G\n\x0eprovider_units\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x46\n\x0crune_address\x18\x03 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12\x44\n\x0brune_amount\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x45\n\x0c\x61sset_amount\x18\x05 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12M\n\nrune_tx_id\x18\x06 \x01(\tB9\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x08RuneTxID\x12O\n\x0b\x61sset_tx_id\x18\x07 \x01(\tB:\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\tAssetTxID\x12G\n\rasset_address\x18\x08 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\"\xcc\x03\n\rEventWithdraw\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12G\n\x0eprovider_units\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x14\n\x0c\x62\x61sis_points\x18\x03 \x01(\x03\x12\x41\n\tasymmetry\x18\x04 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x1f\n\x05in_tx\x18\x05 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\x12\x43\n\nemit_asset\x18\x06 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x42\n\temit_rune\x18\x07 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12L\n\x13imp_loss_protection\x18\x08 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"\xab\x04\n\x15\x45ventPendingLiquidity\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x31\n\x0cpending_type\x18\x02 \x01(\x0e\x32\x1b.types.PendingLiquidityType\x12\x46\n\x0crune_address\x18\x03 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12\x44\n\x0brune_amount\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12G\n\rasset_address\x18\x05 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12\x45\n\x0c\x61sset_amount\x18\x06 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12M\n\nrune_tx_id\x18\x07 \x01(\tB9\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x08RuneTxID\x12O\n\x0b\x61sset_tx_id\x18\x08 \x01(\tB:\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\tAssetTxID\"Q\n\x0b\x45ventDonate\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x1f\n\x05in_tx\x18\x02 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\"Q\n\tEventPool\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12!\n\x06Status\x18\x02 \x01(\x0e\x32\x11.types.PoolStatus\"=\n\x07PoolAmt\x12\"\n\x05\x61sset\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"\x80\x01\n\x0c\x45ventRewards\x12\x44\n\x0b\x62ond_reward\x18\x01 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12*\n\x0cpool_rewards\x18\x02 \x03(\x0b\x32\x0e.types.PoolAmtB\x04\xc8\xde\x1f\x00\"l\n\x0b\x45ventRefund\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x1f\n\x05in_tx\x18\x03 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\x12\x1e\n\x03\x66\x65\x65\x18\x04 \x01(\x0b\x32\x0b.common.FeeB\x04\xc8\xde\x1f\x00\"\x91\x01\n\tEventBond\x12?\n\x06\x61mount\x18\x01 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\"\n\tbond_type\x18\x02 \x01(\x0e\x32\x0f.types.BondType\x12\x1f\n\x05tx_in\x18\x03 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\"\xc3\x01\n\x07GasPool\x12\"\n\x05\x61sset\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x41\n\x08rune_amt\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x42\n\tasset_amt\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\r\n\x05\x63ount\x18\x04 \x01(\x03\"/\n\x08\x45ventGas\x12#\n\x05pools\x18\x01 \x03(\x0b\x32\x0e.types.GasPoolB\x04\xc8\xde\x1f\x00\"m\n\x0c\x45ventReserve\x12<\n\x13reserve_contributor\x18\x01 \x01(\x0b\x32\x19.types.ReserveContributorB\x04\xc8\xde\x1f\x00\x12\x1f\n\x05in_tx\x18\x02 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\"@\n\x16\x45ventScheduledOutbound\x12&\n\x06out_tx\x18\x01 \x01(\x0b\x32\x10.types.TxOutItemB\x04\xc8\xde\x1f\x00\":\n\rEventSecurity\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x1c\n\x02tx\x18\x02 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\"[\n\nEventSlash\x12!\n\x04pool\x18\x01 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12*\n\x0cslash_amount\x18\x02 \x03(\x0b\x32\x0e.types.PoolAmtB\x04\xc8\xde\x1f\x00\"\x84\x01\n\x0b\x45ventErrata\x12\x44\n\x05tx_id\x18\x01 \x01(\tB5\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x04TxID\x12/\n\x05pools\x18\x02 \x03(\x0b\x32\x0e.types.PoolModB\x10\xaa\xdf\x1f\x08PoolMods\xc8\xde\x1f\x00\"\xb6\x01\n\x08\x45ventFee\x12\x44\n\x05tx_id\x18\x01 \x01(\tB5\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x04TxID\x12\x1e\n\x03\x66\x65\x65\x18\x02 \x01(\x0b\x32\x0b.common.FeeB\x04\xc8\xde\x1f\x00\x12\x44\n\x0bsynth_units\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"x\n\rEventOutbound\x12I\n\x08in_tx_id\x18\x01 \x01(\tB7\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x06InTxID\x12\x1c\n\x02tx\x18\x02 \x01(\x0b\x32\n.common.TxB\x04\xc8\xde\x1f\x00\"t\n\x14\x45ventTssKeygenMetric\x12@\n\x07pub_key\x18\x01 \x01(\tB/\xfa\xde\x1f+gitlab.com/thorchain/thornode/common.PubKey\x12\x1a\n\x12median_duration_ms\x18\x02 \x01(\x03\"y\n\x15\x45ventTssKeysignMetric\x12\x44\n\x05tx_id\x18\x01 \x01(\tB5\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x04TxID\x12\x1a\n\x12median_duration_ms\x18\x02 \x01(\x03\"\x80\x01\n\x0f\x45ventSlashPoint\x12G\n\x0cnode_address\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x14\n\x0cslash_points\x18\x02 \x01(\x03\x12\x0e\n\x06reason\x18\x03 \x01(\t\"T\n\x17\x45ventPoolBalanceChanged\x12)\n\x0bpool_change\x18\x01 \x01(\x0b\x32\x0e.types.PoolModB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\x84\x02\n\x0b\x45ventSwitch\x12\x45\n\nto_address\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x46\n\x0c\x66rom_address\x18\x02 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12 \n\x04\x62urn\x18\x03 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12\x44\n\x05tx_id\x18\x04 \x01(\tB5\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x04TxID\"\xc6\x02\n\x0e\x45ventSwitchV87\x12\x45\n\nto_address\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x46\n\x0c\x66rom_address\x18\x02 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12 \n\x04\x62urn\x18\x03 \x01(\x0b\x32\x0c.common.CoinB\x04\xc8\xde\x1f\x00\x12\x44\n\x05tx_id\x18\x04 \x01(\tB5\xfa\xde\x1f)gitlab.com/thorchain/thornode/common.TxID\xe2\xde\x1f\x04TxID\x12=\n\x04mint\x18\x05 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"\x9a\x01\n\rEventMintBurn\x12)\n\x06supply\x18\x01 \x01(\x0e\x32\x19.types.MintBurnSupplyType\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12?\n\x06\x61mount\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x0e\n\x06reason\x18\x04 \x01(\t\"\x86\x03\n\rEventLoanOpen\x12\x46\n\rcollateral_up\x18\x01 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12-\n\x10\x63ollateral_asset\x18\x02 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12P\n\x17\x63ollateralization_ratio\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12@\n\x07\x64\x65\x62t_up\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12?\n\x05owner\x18\x05 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12)\n\x0ctarget_asset\x18\x06 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\"\x92\x02\n\x12\x45ventLoanRepayment\x12H\n\x0f\x63ollateral_down\x18\x01 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12-\n\x10\x63ollateral_asset\x18\x02 \x01(\x0b\x32\r.common.AssetB\x04\xc8\xde\x1f\x00\x12\x42\n\tdebt_down\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12?\n\x05owner\x18\x04 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\"\xff\x02\n\rEventTHORName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x05\x63hain\x18\x02 \x01(\tB.\xfa\xde\x1f*gitlab.com/thorchain/thornode/common.Chain\x12\x41\n\x07\x61\x64\x64ress\x18\x03 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.Address\x12I\n\x10registration_fee\x18\x04 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x41\n\x08\x66und_amt\x18\x05 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12\x0e\n\x06\x65xpire\x18\x06 \x01(\x03\x12@\n\x05owner\x18\x07 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\"+\n\rEventSetMimir\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"@\n\x11\x45ventSetNodeMimir\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\x1f\n\x0c\x45ventVersion\x12\x0f\n\x07version\x18\x01 \x01(\t*-\n\x14PendingLiquidityType\x12\x07\n\x03\x61\x64\x64\x10\x00\x12\x0c\n\x08withdraw\x10\x01*L\n\x08\x42ondType\x12\r\n\tbond_paid\x10\x00\x12\x11\n\rbond_returned\x10\x01\x12\x0f\n\x0b\x62ond_reward\x10\x02\x12\r\n\tbond_cost\x10\x03*(\n\x12MintBurnSupplyType\x12\x08\n\x04mint\x10\x00\x12\x08\n\x04\x62urn\x10\x01\x42\x31Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.type_events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _POOLMOD.fields_by_name['asset']._options = None
  _POOLMOD.fields_by_name['asset']._serialized_options = b'\310\336\037\000'
  _POOLMOD.fields_by_name['rune_amt']._options = None
  _POOLMOD.fields_by_name['rune_amt']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _POOLMOD.fields_by_name['asset_amt']._options = None
  _POOLMOD.fields_by_name['asset_amt']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLIMITORDER.fields_by_name['source']._options = None
  _EVENTLIMITORDER.fields_by_name['source']._serialized_options = b'\310\336\037\000'
  _EVENTLIMITORDER.fields_by_name['target']._options = None
  _EVENTLIMITORDER.fields_by_name['target']._serialized_options = b'\310\336\037\000'
  _EVENTLIMITORDER.fields_by_name['tx_id']._options = None
  _EVENTLIMITORDER.fields_by_name['tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\004TxID'
  _EVENTSWAP.fields_by_name['pool']._options = None
  _EVENTSWAP.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _EVENTSWAP.fields_by_name['swap_target']._options = None
  _EVENTSWAP.fields_by_name['swap_target']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTSWAP.fields_by_name['swap_slip']._options = None
  _EVENTSWAP.fields_by_name['swap_slip']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTSWAP.fields_by_name['liquidity_fee']._options = None
  _EVENTSWAP.fields_by_name['liquidity_fee']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTSWAP.fields_by_name['liquidity_fee_in_rune']._options = None
  _EVENTSWAP.fields_by_name['liquidity_fee_in_rune']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTSWAP.fields_by_name['in_tx']._options = None
  _EVENTSWAP.fields_by_name['in_tx']._serialized_options = b'\310\336\037\000'
  _EVENTSWAP.fields_by_name['out_txs']._options = None
  _EVENTSWAP.fields_by_name['out_txs']._serialized_options = b'\310\336\037\000'
  _EVENTSWAP.fields_by_name['emit_asset']._options = None
  _EVENTSWAP.fields_by_name['emit_asset']._serialized_options = b'\310\336\037\000'
  _EVENTSWAP.fields_by_name['synth_units']._options = None
  _EVENTSWAP.fields_by_name['synth_units']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTADDLIQUIDITY.fields_by_name['pool']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _EVENTADDLIQUIDITY.fields_by_name['provider_units']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['provider_units']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTADDLIQUIDITY.fields_by_name['rune_address']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['rune_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTADDLIQUIDITY.fields_by_name['rune_amount']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['rune_amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTADDLIQUIDITY.fields_by_name['asset_amount']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['asset_amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTADDLIQUIDITY.fields_by_name['rune_tx_id']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['rune_tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\010RuneTxID'
  _EVENTADDLIQUIDITY.fields_by_name['asset_tx_id']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['asset_tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\tAssetTxID'
  _EVENTADDLIQUIDITY.fields_by_name['asset_address']._options = None
  _EVENTADDLIQUIDITY.fields_by_name['asset_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTWITHDRAW.fields_by_name['pool']._options = None
  _EVENTWITHDRAW.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _EVENTWITHDRAW.fields_by_name['provider_units']._options = None
  _EVENTWITHDRAW.fields_by_name['provider_units']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTWITHDRAW.fields_by_name['asymmetry']._options = None
  _EVENTWITHDRAW.fields_by_name['asymmetry']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTWITHDRAW.fields_by_name['in_tx']._options = None
  _EVENTWITHDRAW.fields_by_name['in_tx']._serialized_options = b'\310\336\037\000'
  _EVENTWITHDRAW.fields_by_name['emit_asset']._options = None
  _EVENTWITHDRAW.fields_by_name['emit_asset']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTWITHDRAW.fields_by_name['emit_rune']._options = None
  _EVENTWITHDRAW.fields_by_name['emit_rune']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTWITHDRAW.fields_by_name['imp_loss_protection']._options = None
  _EVENTWITHDRAW.fields_by_name['imp_loss_protection']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTPENDINGLIQUIDITY.fields_by_name['pool']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _EVENTPENDINGLIQUIDITY.fields_by_name['rune_address']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['rune_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTPENDINGLIQUIDITY.fields_by_name['rune_amount']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['rune_amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTPENDINGLIQUIDITY.fields_by_name['asset_address']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['asset_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTPENDINGLIQUIDITY.fields_by_name['asset_amount']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['asset_amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTPENDINGLIQUIDITY.fields_by_name['rune_tx_id']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['rune_tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\010RuneTxID'
  _EVENTPENDINGLIQUIDITY.fields_by_name['asset_tx_id']._options = None
  _EVENTPENDINGLIQUIDITY.fields_by_name['asset_tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\tAssetTxID'
  _EVENTDONATE.fields_by_name['pool']._options = None
  _EVENTDONATE.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _EVENTDONATE.fields_by_name['in_tx']._options = None
  _EVENTDONATE.fields_by_name['in_tx']._serialized_options = b'\310\336\037\000'
  _EVENTPOOL.fields_by_name['pool']._options = None
  _EVENTPOOL.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _POOLAMT.fields_by_name['asset']._options = None
  _POOLAMT.fields_by_name['asset']._serialized_options = b'\310\336\037\000'
  _EVENTREWARDS.fields_by_name['bond_reward']._options = None
  _EVENTREWARDS.fields_by_name['bond_reward']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTREWARDS.fields_by_name['pool_rewards']._options = None
  _EVENTREWARDS.fields_by_name['pool_rewards']._serialized_options = b'\310\336\037\000'
  _EVENTREFUND.fields_by_name['in_tx']._options = None
  _EVENTREFUND.fields_by_name['in_tx']._serialized_options = b'\310\336\037\000'
  _EVENTREFUND.fields_by_name['fee']._options = None
  _EVENTREFUND.fields_by_name['fee']._serialized_options = b'\310\336\037\000'
  _EVENTBOND.fields_by_name['amount']._options = None
  _EVENTBOND.fields_by_name['amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTBOND.fields_by_name['tx_in']._options = None
  _EVENTBOND.fields_by_name['tx_in']._serialized_options = b'\310\336\037\000'
  _GASPOOL.fields_by_name['asset']._options = None
  _GASPOOL.fields_by_name['asset']._serialized_options = b'\310\336\037\000'
  _GASPOOL.fields_by_name['rune_amt']._options = None
  _GASPOOL.fields_by_name['rune_amt']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _GASPOOL.fields_by_name['asset_amt']._options = None
  _GASPOOL.fields_by_name['asset_amt']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTGAS.fields_by_name['pools']._options = None
  _EVENTGAS.fields_by_name['pools']._serialized_options = b'\310\336\037\000'
  _EVENTRESERVE.fields_by_name['reserve_contributor']._options = None
  _EVENTRESERVE.fields_by_name['reserve_contributor']._serialized_options = b'\310\336\037\000'
  _EVENTRESERVE.fields_by_name['in_tx']._options = None
  _EVENTRESERVE.fields_by_name['in_tx']._serialized_options = b'\310\336\037\000'
  _EVENTSCHEDULEDOUTBOUND.fields_by_name['out_tx']._options = None
  _EVENTSCHEDULEDOUTBOUND.fields_by_name['out_tx']._serialized_options = b'\310\336\037\000'
  _EVENTSECURITY.fields_by_name['tx']._options = None
  _EVENTSECURITY.fields_by_name['tx']._serialized_options = b'\310\336\037\000'
  _EVENTSLASH.fields_by_name['pool']._options = None
  _EVENTSLASH.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _EVENTSLASH.fields_by_name['slash_amount']._options = None
  _EVENTSLASH.fields_by_name['slash_amount']._serialized_options = b'\310\336\037\000'
  _EVENTERRATA.fields_by_name['tx_id']._options = None
  _EVENTERRATA.fields_by_name['tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\004TxID'
  _EVENTERRATA.fields_by_name['pools']._options = None
  _EVENTERRATA.fields_by_name['pools']._serialized_options = b'\252\337\037\010PoolMods\310\336\037\000'
  _EVENTFEE.fields_by_name['tx_id']._options = None
  _EVENTFEE.fields_by_name['tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\004TxID'
  _EVENTFEE.fields_by_name['fee']._options = None
  _EVENTFEE.fields_by_name['fee']._serialized_options = b'\310\336\037\000'
  _EVENTFEE.fields_by_name['synth_units']._options = None
  _EVENTFEE.fields_by_name['synth_units']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTOUTBOUND.fields_by_name['in_tx_id']._options = None
  _EVENTOUTBOUND.fields_by_name['in_tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\006InTxID'
  _EVENTOUTBOUND.fields_by_name['tx']._options = None
  _EVENTOUTBOUND.fields_by_name['tx']._serialized_options = b'\310\336\037\000'
  _EVENTTSSKEYGENMETRIC.fields_by_name['pub_key']._options = None
  _EVENTTSSKEYGENMETRIC.fields_by_name['pub_key']._serialized_options = b'\372\336\037+gitlab.com/thorchain/thornode/common.PubKey'
  _EVENTTSSKEYSIGNMETRIC.fields_by_name['tx_id']._options = None
  _EVENTTSSKEYSIGNMETRIC.fields_by_name['tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\004TxID'
  _EVENTSLASHPOINT.fields_by_name['node_address']._options = None
  _EVENTSLASHPOINT.fields_by_name['node_address']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _EVENTPOOLBALANCECHANGED.fields_by_name['pool_change']._options = None
  _EVENTPOOLBALANCECHANGED.fields_by_name['pool_change']._serialized_options = b'\310\336\037\000'
  _EVENTSWITCH.fields_by_name['to_address']._options = None
  _EVENTSWITCH.fields_by_name['to_address']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _EVENTSWITCH.fields_by_name['from_address']._options = None
  _EVENTSWITCH.fields_by_name['from_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTSWITCH.fields_by_name['burn']._options = None
  _EVENTSWITCH.fields_by_name['burn']._serialized_options = b'\310\336\037\000'
  _EVENTSWITCH.fields_by_name['tx_id']._options = None
  _EVENTSWITCH.fields_by_name['tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\004TxID'
  _EVENTSWITCHV87.fields_by_name['to_address']._options = None
  _EVENTSWITCHV87.fields_by_name['to_address']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _EVENTSWITCHV87.fields_by_name['from_address']._options = None
  _EVENTSWITCHV87.fields_by_name['from_address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTSWITCHV87.fields_by_name['burn']._options = None
  _EVENTSWITCHV87.fields_by_name['burn']._serialized_options = b'\310\336\037\000'
  _EVENTSWITCHV87.fields_by_name['tx_id']._options = None
  _EVENTSWITCHV87.fields_by_name['tx_id']._serialized_options = b'\372\336\037)gitlab.com/thorchain/thornode/common.TxID\342\336\037\004TxID'
  _EVENTSWITCHV87.fields_by_name['mint']._options = None
  _EVENTSWITCHV87.fields_by_name['mint']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTMINTBURN.fields_by_name['amount']._options = None
  _EVENTMINTBURN.fields_by_name['amount']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLOANOPEN.fields_by_name['collateral_up']._options = None
  _EVENTLOANOPEN.fields_by_name['collateral_up']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLOANOPEN.fields_by_name['collateral_asset']._options = None
  _EVENTLOANOPEN.fields_by_name['collateral_asset']._serialized_options = b'\310\336\037\000'
  _EVENTLOANOPEN.fields_by_name['collateralization_ratio']._options = None
  _EVENTLOANOPEN.fields_by_name['collateralization_ratio']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLOANOPEN.fields_by_name['debt_up']._options = None
  _EVENTLOANOPEN.fields_by_name['debt_up']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLOANOPEN.fields_by_name['owner']._options = None
  _EVENTLOANOPEN.fields_by_name['owner']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTLOANOPEN.fields_by_name['target_asset']._options = None
  _EVENTLOANOPEN.fields_by_name['target_asset']._serialized_options = b'\310\336\037\000'
  _EVENTLOANREPAYMENT.fields_by_name['collateral_down']._options = None
  _EVENTLOANREPAYMENT.fields_by_name['collateral_down']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLOANREPAYMENT.fields_by_name['collateral_asset']._options = None
  _EVENTLOANREPAYMENT.fields_by_name['collateral_asset']._serialized_options = b'\310\336\037\000'
  _EVENTLOANREPAYMENT.fields_by_name['debt_down']._options = None
  _EVENTLOANREPAYMENT.fields_by_name['debt_down']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTLOANREPAYMENT.fields_by_name['owner']._options = None
  _EVENTLOANREPAYMENT.fields_by_name['owner']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTTHORNAME.fields_by_name['chain']._options = None
  _EVENTTHORNAME.fields_by_name['chain']._serialized_options = b'\372\336\037*gitlab.com/thorchain/thornode/common.Chain'
  _EVENTTHORNAME.fields_by_name['address']._options = None
  _EVENTTHORNAME.fields_by_name['address']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _EVENTTHORNAME.fields_by_name['registration_fee']._options = None
  _EVENTTHORNAME.fields_by_name['registration_fee']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTTHORNAME.fields_by_name['fund_amt']._options = None
  _EVENTTHORNAME.fields_by_name['fund_amt']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000'
  _EVENTTHORNAME.fields_by_name['owner']._options = None
  _EVENTTHORNAME.fields_by_name['owner']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _PENDINGLIQUIDITYTYPE._serialized_start=6816
  _PENDINGLIQUIDITYTYPE._serialized_end=6861
  _BONDTYPE._serialized_start=6863
  _BONDTYPE._serialized_end=6939
  _MINTBURNSUPPLYTYPE._serialized_start=6941
  _MINTBURNSUPPLYTYPE._serialized_end=6981
  _POOLMOD._serialized_start=277
  _POOLMOD._serialized_end=494
  _EVENTLIMITORDER._serialized_start=497
  _EVENTLIMITORDER._serialized_end=656
  _EVENTSWAP._serialized_start=659
  _EVENTSWAP._serialized_end=1173
  _EVENTADDLIQUIDITY._serialized_start=1176
  _EVENTADDLIQUIDITY._serialized_end=1749
  _EVENTWITHDRAW._serialized_start=1752
  _EVENTWITHDRAW._serialized_end=2212
  _EVENTPENDINGLIQUIDITY._serialized_start=2215
  _EVENTPENDINGLIQUIDITY._serialized_end=2770
  _EVENTDONATE._serialized_start=2772
  _EVENTDONATE._serialized_end=2853
  _EVENTPOOL._serialized_start=2855
  _EVENTPOOL._serialized_end=2936
  _POOLAMT._serialized_start=2938
  _POOLAMT._serialized_end=2999
  _EVENTREWARDS._serialized_start=3002
  _EVENTREWARDS._serialized_end=3130
  _EVENTREFUND._serialized_start=3132
  _EVENTREFUND._serialized_end=3240
  _EVENTBOND._serialized_start=3243
  _EVENTBOND._serialized_end=3388
  _GASPOOL._serialized_start=3391
  _GASPOOL._serialized_end=3586
  _EVENTGAS._serialized_start=3588
  _EVENTGAS._serialized_end=3635
  _EVENTRESERVE._serialized_start=3637
  _EVENTRESERVE._serialized_end=3746
  _EVENTSCHEDULEDOUTBOUND._serialized_start=3748
  _EVENTSCHEDULEDOUTBOUND._serialized_end=3812
  _EVENTSECURITY._serialized_start=3814
  _EVENTSECURITY._serialized_end=3872
  _EVENTSLASH._serialized_start=3874
  _EVENTSLASH._serialized_end=3965
  _EVENTERRATA._serialized_start=3968
  _EVENTERRATA._serialized_end=4100
  _EVENTFEE._serialized_start=4103
  _EVENTFEE._serialized_end=4285
  _EVENTOUTBOUND._serialized_start=4287
  _EVENTOUTBOUND._serialized_end=4407
  _EVENTTSSKEYGENMETRIC._serialized_start=4409
  _EVENTTSSKEYGENMETRIC._serialized_end=4525
  _EVENTTSSKEYSIGNMETRIC._serialized_start=4527
  _EVENTTSSKEYSIGNMETRIC._serialized_end=4648
  _EVENTSLASHPOINT._serialized_start=4651
  _EVENTSLASHPOINT._serialized_end=4779
  _EVENTPOOLBALANCECHANGED._serialized_start=4781
  _EVENTPOOLBALANCECHANGED._serialized_end=4865
  _EVENTSWITCH._serialized_start=4868
  _EVENTSWITCH._serialized_end=5128
  _EVENTSWITCHV87._serialized_start=5131
  _EVENTSWITCHV87._serialized_end=5457
  _EVENTMINTBURN._serialized_start=5460
  _EVENTMINTBURN._serialized_end=5614
  _EVENTLOANOPEN._serialized_start=5617
  _EVENTLOANOPEN._serialized_end=6007
  _EVENTLOANREPAYMENT._serialized_start=6010
  _EVENTLOANREPAYMENT._serialized_end=6284
  _EVENTTHORNAME._serialized_start=6287
  _EVENTTHORNAME._serialized_end=6670
  _EVENTSETMIMIR._serialized_start=6672
  _EVENTSETMIMIR._serialized_end=6715
  _EVENTSETNODEMIMIR._serialized_start=6717
  _EVENTSETNODEMIMIR._serialized_end=6781
  _EVENTVERSION._serialized_start=6783
  _EVENTVERSION._serialized_end=6814
# @@protoc_insertion_point(module_scope)