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
class MsgNodePauseChain(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    value: builtins.int
    signer: builtins.bytes
    def __init__(
        self,
        *,
        value: builtins.int = ...,
        signer: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["signer", b"signer", "value", b"value"]) -> None: ...

global___MsgNodePauseChain = MsgNodePauseChain
