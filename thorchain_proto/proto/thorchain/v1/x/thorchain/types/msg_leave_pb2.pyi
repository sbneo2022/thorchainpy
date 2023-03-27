"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import thorchain.v1.common.common_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgLeave(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_FIELD_NUMBER: builtins.int
    NODE_ADDRESS_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    @property
    def tx(self) -> thorchain.v1.common.common_pb2.Tx: ...
    node_address: builtins.bytes
    signer: builtins.bytes
    def __init__(
        self,
        *,
        tx: thorchain.v1.common.common_pb2.Tx | None = ...,
        node_address: builtins.bytes = ...,
        signer: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node_address", b"node_address", "signer", b"signer", "tx", b"tx"]) -> None: ...

global___MsgLeave = MsgLeave