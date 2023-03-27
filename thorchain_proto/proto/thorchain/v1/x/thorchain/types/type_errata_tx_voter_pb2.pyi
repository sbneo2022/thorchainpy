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

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ErrataTxVoter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_ID_FIELD_NUMBER: builtins.int
    CHAIN_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    SIGNERS_FIELD_NUMBER: builtins.int
    tx_id: builtins.str
    chain: builtins.str
    block_height: builtins.int
    @property
    def signers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        tx_id: builtins.str = ...,
        chain: builtins.str = ...,
        block_height: builtins.int = ...,
        signers: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height", b"block_height", "chain", b"chain", "signers", b"signers", "tx_id", b"tx_id"]) -> None: ...

global___ErrataTxVoter = ErrataTxVoter