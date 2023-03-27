"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgErrataTx(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_ID_FIELD_NUMBER: builtins.int
    CHAIN_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    tx_id: builtins.str
    chain: builtins.str
    signer: builtins.bytes
    def __init__(
        self,
        *,
        tx_id: builtins.str = ...,
        chain: builtins.str = ...,
        signer: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain", b"chain", "signer", b"signer", "tx_id", b"tx_id"]) -> None: ...

global___MsgErrataTx = MsgErrataTx