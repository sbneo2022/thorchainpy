# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/type_chain_contract.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8thorchain/v1/x/thorchain/types/type_chain_contract.proto\x12\x05types\x1a\x14gogoproto/gogo.proto\"\x90\x01\n\rChainContract\x12=\n\x05\x63hain\x18\x01 \x01(\tB.\xfa\xde\x1f*gitlab.com/thorchain/thornode/common.Chain\x12@\n\x06router\x18\x02 \x01(\tB0\xfa\xde\x1f,gitlab.com/thorchain/thornode/common.AddressB=Z/gitlab.com/thorchain/thornode/x/thorchain/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00\xc8\xe1\x1e\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.type_chain_contract_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types\330\341\036\000\200\342\036\000\310\341\036\000'
  _CHAINCONTRACT.fields_by_name['chain']._options = None
  _CHAINCONTRACT.fields_by_name['chain']._serialized_options = b'\372\336\037*gitlab.com/thorchain/thornode/common.Chain'
  _CHAINCONTRACT.fields_by_name['router']._options = None
  _CHAINCONTRACT.fields_by_name['router']._serialized_options = b'\372\336\037,gitlab.com/thorchain/thornode/common.Address'
  _CHAINCONTRACT._serialized_start=90
  _CHAINCONTRACT._serialized_end=234
# @@protoc_insertion_point(module_scope)