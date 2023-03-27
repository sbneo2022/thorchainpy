"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import thorchain.v1.x.thorchain.types.type_observed_tx_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgObservedTxIn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TXS_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    @property
    def txs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thorchain.v1.x.thorchain.types.type_observed_tx_pb2.ObservedTx]: ...
    signer: builtins.bytes
    def __init__(
        self,
        *,
        txs: collections.abc.Iterable[thorchain.v1.x.thorchain.types.type_observed_tx_pb2.ObservedTx] | None = ...,
        signer: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["signer", b"signer", "txs", b"txs"]) -> None: ...

global___MsgObservedTxIn = MsgObservedTxIn