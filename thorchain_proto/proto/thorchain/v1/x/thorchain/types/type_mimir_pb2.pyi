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
class NodeMimir(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    key: builtins.str
    value: builtins.int
    signer: builtins.bytes
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        value: builtins.int = ...,
        signer: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "signer", b"signer", "value", b"value"]) -> None: ...

global___NodeMimir = NodeMimir

@typing_extensions.final
class NodeMimirs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIMIRS_FIELD_NUMBER: builtins.int
    @property
    def mimirs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NodeMimir]: ...
    def __init__(
        self,
        *,
        mimirs: collections.abc.Iterable[global___NodeMimir] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mimirs", b"mimirs"]) -> None: ...

global___NodeMimirs = NodeMimirs