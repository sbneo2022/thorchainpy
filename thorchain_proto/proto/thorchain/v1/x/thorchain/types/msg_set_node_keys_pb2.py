# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thorchain/v1/x/thorchain/types/msg_set_node_keys.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from thorchain.v1.common import common_pb2 as thorchain_dot_v1_dot_common_dot_common__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6thorchain/v1/x/thorchain/types/msg_set_node_keys.proto\x12\x05types\x1a thorchain/v1/common/common.proto\x1a\x14gogoproto/gogo.proto\"\xa5\x01\n\x0eMsgSetNodeKeys\x12\x30\n\x0fpub_key_set_set\x18\x01 \x01(\x0b\x32\x11.common.PubKeySetB\x04\xc8\xde\x1f\x00\x12\x1e\n\x16validator_cons_pub_key\x18\x02 \x01(\t\x12\x41\n\x06signer\x18\x03 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB1Z/gitlab.com/thorchain/thornode/x/thorchain/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thorchain.v1.x.thorchain.types.msg_set_node_keys_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/gitlab.com/thorchain/thornode/x/thorchain/types'
  _MSGSETNODEKEYS.fields_by_name['pub_key_set_set']._options = None
  _MSGSETNODEKEYS.fields_by_name['pub_key_set_set']._serialized_options = b'\310\336\037\000'
  _MSGSETNODEKEYS.fields_by_name['signer']._options = None
  _MSGSETNODEKEYS.fields_by_name['signer']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _MSGSETNODEKEYS._serialized_start=122
  _MSGSETNODEKEYS._serialized_end=287
# @@protoc_insertion_point(module_scope)