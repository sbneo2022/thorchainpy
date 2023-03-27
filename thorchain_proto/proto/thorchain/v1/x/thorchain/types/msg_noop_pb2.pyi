"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import thorchain.v1.x.thorchain.types.type_observed_tx_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgNoOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBSERVED_TX_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    @property
    def observed_tx(self) -> thorchain.v1.x.thorchain.types.type_observed_tx_pb2.ObservedTx: ...
    signer: builtins.bytes
    action: builtins.str
    def __init__(
        self,
        *,
        observed_tx: thorchain.v1.x.thorchain.types.type_observed_tx_pb2.ObservedTx | None = ...,
        signer: builtins.bytes = ...,
        action: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["observed_tx", b"observed_tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "observed_tx", b"observed_tx", "signer", b"signer"]) -> None: ...

global___MsgNoOp = MsgNoOp
