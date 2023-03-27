# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.x.thorchain.types import type_pool_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__pool__pb2
from thorchain.v1.x.thorchain.types import type_chain_contract_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__chain__contract__pb2
from thorchain.v1.x.thorchain.types import type_network_fee_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__network__fee__pb2
from thorchain.v1.x.thorchain.types import msg_swap_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_msg__swap__pb2
from thorchain.v1.x.thorchain.types import type_network_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__network__pb2
from thorchain.v1.x.thorchain.types import type_pol_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__pol__pb2
from thorchain.v1.x.thorchain.types import type_reserve_contributor_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__reserve__contributor__pb2
from thorchain.v1.x.thorchain.types import type_vault_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__vault__pb2
from thorchain.v1.x.thorchain.types import type_tx_out_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__tx__out__pb2
from thorchain.v1.x.thorchain.types import type_node_account_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__node__account__pb2
from thorchain.v1.x.thorchain.types import type_observed_tx_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__observed__tx__pb2
from thorchain.v1.x.thorchain.types import type_liquidity_provider_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__liquidity__provider__pb2
from thorchain.v1.x.thorchain.types import type_thorname_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__thorname__pb2
from thorchain.v1.x.thorchain.types import type_loan_pb2 as thorchain_dot_v1_dot_x_dot_thorchain_dot_types_dot_type__loan__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&thorchain/v1/x/thorchain/genesis.proto\x12\tthorchain\x1a.thorchain/v1/x/thorchain/types/type_pool.proto\x1a\x38thorchain/v1/x/thorchain/types/type_chain_contract.proto\x1a\x35thorchain/v1/x/thorchain/types/type_network_fee.proto\x1a-thorchain/v1/x/thorchain/types/msg_swap.proto\x1a\x31thorchain/v1/x/thorchain/types/type_network.proto\x1a-thorchain/v1/x/thorchain/types/type_pol.proto\x1a=thorchain/v1/x/thorchain/types/type_reserve_contributor.proto\x1a/thorchain/v1/x/thorchain/types/type_vault.proto\x1a\x30thorchain/v1/x/thorchain/types/type_tx_out.proto\x1a\x36thorchain/v1/x/thorchain/types/type_node_account.proto\x1a\x35thorchain/v1/x/thorchain/types/type_observed_tx.proto\x1a<thorchain/v1/x/thorchain/types/type_liquidity_provider.proto\x1a\x32thorchain/v1/x/thorchain/types/type_thorname.proto\x1a.thorchain/v1/x/thorchain/types/type_loan.proto\x1a\x14gogoproto/gogo.proto\"0\n\x0flastChainHeight\x12\r\n\x05\x63hain\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x03\"#\n\x05mimir\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\"\xed\n\n\x0cGenesisState\x12 \n\x05pools\x18\x01 \x03(\x0b\x32\x0b.types.PoolB\x04\xc8\xde\x1f\x00\x12\x81\x01\n\x13liquidity_providers\x18\x02 \x03(\x0b\x32\x18.types.LiquidityProviderBJ\xaa\xdf\x1f\x42gitlab.com/thorchain/thornode/x/thorchain/types.LiquidityProviders\xc8\xde\x1f\x00\x12\x7f\n\x15observed_tx_in_voters\x18\x03 \x03(\x0b\x32\x16.types.ObservedTxVoterBH\xaa\xdf\x1f@gitlab.com/thorchain/thornode/x/thorchain/types.ObservedTxVoters\xc8\xde\x1f\x00\x12\x80\x01\n\x16observed_tx_out_voters\x18\x04 \x03(\x0b\x32\x16.types.ObservedTxVoterBH\xaa\xdf\x1f@gitlab.com/thorchain/thornode/x/thorchain/types.ObservedTxVoters\xc8\xde\x1f\x00\x12#\n\x07tx_outs\x18\x05 \x03(\x0b\x32\x0c.types.TxOutB\x04\xc8\xde\x1f\x00\x12o\n\rnode_accounts\x18\x06 \x03(\x0b\x32\x12.types.NodeAccountBD\xaa\xdf\x1f<gitlab.com/thorchain/thornode/x/thorchain/types.NodeAccounts\xc8\xde\x1f\x00\x12\\\n\x06vaults\x18\x07 \x03(\x0b\x32\x0c.types.VaultB>\xaa\xdf\x1f\x36gitlab.com/thorchain/thornode/x/thorchain/types.Vaults\xc8\xde\x1f\x00\x12\x0f\n\x07reserve\x18\x08 \x01(\x04\x12\x1a\n\x12last_signed_height\x18\n \x01(\x03\x12<\n\x12last_chain_heights\x18\x0b \x03(\x0b\x32\x1a.thorchain.lastChainHeightB\x04\xc8\xde\x1f\x00\x12\x84\x01\n\x14reserve_contributors\x18\x0c \x03(\x0b\x32\x19.types.ReserveContributorBK\xaa\xdf\x1f\x43gitlab.com/thorchain/thornode/x/thorchain/types.ReserveContributors\xc8\xde\x1f\x00\x12%\n\x07network\x18\r \x01(\x0b\x32\x0e.types.NetworkB\x04\xc8\xde\x1f\x00\x12\'\n\tmsg_swaps\x18\x13 \x03(\x0b\x32\x0e.types.MsgSwapB\x04\xc8\xde\x1f\x00\x12-\n\x0cnetwork_fees\x18\x14 \x03(\x0b\x32\x11.types.NetworkFeeB\x04\xc8\xde\x1f\x00\x12\x33\n\x0f\x63hain_contracts\x18\x16 \x03(\x0b\x32\x14.types.ChainContractB\x04\xc8\xde\x1f\x00\x12(\n\tTHORNames\x18\x17 \x03(\x0b\x32\x0f.types.THORNameB\x04\xc8\xde\x1f\x00\x12&\n\x06mimirs\x18\x18 \x03(\x0b\x32\x10.thorchain.mimirB\x04\xc8\xde\x1f\x00\x12\x15\n\rstore_version\x18\x19 \x01(\x03\x12\x32\n\x0e\x62ond_providers\x18\x1a \x03(\x0b\x32\x14.types.BondProvidersB\x04\xc8\xde\x1f\x00\x12\x30\n\x03POL\x18\x1b \x01(\x0b\x32\x1d.types.ProtocolOwnedLiquidityB\x04\xc8\xde\x1f\x00\x12 \n\x05loans\x18\x1c \x03(\x0b\x32\x0b.types.LoanB\x04\xc8\xde\x1f\x00J\x04\x08\t\x10\nJ\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13J\x04\x08\x15\x10\x16\x42+Z)gitlab.com/thorchain/thornode/x/thorchainb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)gitlab.com/thorchain/thornode/x/thorchain'
  _GENESISSTATE.fields_by_name['pools']._options = None
  _GENESISSTATE.fields_by_name['pools']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['liquidity_providers']._options = None
  _GENESISSTATE.fields_by_name['liquidity_providers']._serialized_options = b'\252\337\037Bgitlab.com/thorchain/thornode/x/thorchain/types.LiquidityProviders\310\336\037\000'
  _GENESISSTATE.fields_by_name['observed_tx_in_voters']._options = None
  _GENESISSTATE.fields_by_name['observed_tx_in_voters']._serialized_options = b'\252\337\037@gitlab.com/thorchain/thornode/x/thorchain/types.ObservedTxVoters\310\336\037\000'
  _GENESISSTATE.fields_by_name['observed_tx_out_voters']._options = None
  _GENESISSTATE.fields_by_name['observed_tx_out_voters']._serialized_options = b'\252\337\037@gitlab.com/thorchain/thornode/x/thorchain/types.ObservedTxVoters\310\336\037\000'
  _GENESISSTATE.fields_by_name['tx_outs']._options = None
  _GENESISSTATE.fields_by_name['tx_outs']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['node_accounts']._options = None
  _GENESISSTATE.fields_by_name['node_accounts']._serialized_options = b'\252\337\037<gitlab.com/thorchain/thornode/x/thorchain/types.NodeAccounts\310\336\037\000'
  _GENESISSTATE.fields_by_name['vaults']._options = None
  _GENESISSTATE.fields_by_name['vaults']._serialized_options = b'\252\337\0376gitlab.com/thorchain/thornode/x/thorchain/types.Vaults\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_chain_heights']._options = None
  _GENESISSTATE.fields_by_name['last_chain_heights']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['reserve_contributors']._options = None
  _GENESISSTATE.fields_by_name['reserve_contributors']._serialized_options = b'\252\337\037Cgitlab.com/thorchain/thornode/x/thorchain/types.ReserveContributors\310\336\037\000'
  _GENESISSTATE.fields_by_name['network']._options = None
  _GENESISSTATE.fields_by_name['network']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['msg_swaps']._options = None
  _GENESISSTATE.fields_by_name['msg_swaps']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['network_fees']._options = None
  _GENESISSTATE.fields_by_name['network_fees']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['chain_contracts']._options = None
  _GENESISSTATE.fields_by_name['chain_contracts']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['THORNames']._options = None
  _GENESISSTATE.fields_by_name['THORNames']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['mimirs']._options = None
  _GENESISSTATE.fields_by_name['mimirs']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['bond_providers']._options = None
  _GENESISSTATE.fields_by_name['bond_providers']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['POL']._options = None
  _GENESISSTATE.fields_by_name['POL']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['loans']._options = None
  _GENESISSTATE.fields_by_name['loans']._serialized_options = b'\310\336\037\000'
  _LASTCHAINHEIGHT._serialized_start=816
  _LASTCHAINHEIGHT._serialized_end=864
  _MIMIR._serialized_start=866
  _MIMIR._serialized_end=901
  _GENESISSTATE._serialized_start=904
  _GENESISSTATE._serialized_end=2293
# @@protoc_insertion_point(module_scope)
