# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_set_ip_address.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7thorchain/v1/x/thorchain/types/msg_set_ip_address.proto\x12\x05types\x1a\x14gogoproto/gogo.proto\"w\n\x0fMsgSetIPAddress\x12!\n\nip_address\x18\x01 \x01(\tB\r\xe2\xde\x1f\tIPAddress\x12\x41\n\x06signer\x18\x02 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_set_ip_address_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGSETIPADDRESS.fields_by_name['ip_address']._options = None
  _MSGSETIPADDRESS.fields_by_name['ip_address']._serialized_options = b'\342\336\037\tIPAddress'
  _MSGSETIPADDRESS.fields_by_name['signer']._options = None
  _MSGSETIPADDRESS.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGSETIPADDRESS._serialized_start=88
  _MSGSETIPADDRESS._serialized_end=207
# @@protoc_insertion_point(module_scope)