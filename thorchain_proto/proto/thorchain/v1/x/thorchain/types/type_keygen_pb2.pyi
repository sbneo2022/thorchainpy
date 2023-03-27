"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _KeygenType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _KeygenTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KeygenType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UnknownKeygen: _KeygenType.ValueType  # 0
    AsgardKeygen: _KeygenType.ValueType  # 1
    YggdrasilKeygen: _KeygenType.ValueType  # 2

class KeygenType(_KeygenType, metaclass=_KeygenTypeEnumTypeWrapper): ...

UnknownKeygen: KeygenType.ValueType  # 0
AsgardKeygen: KeygenType.ValueType  # 1
YggdrasilKeygen: KeygenType.ValueType  # 2
global___KeygenType = KeygenType

@typing_extensions.final
class Keygen(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    id: builtins.str
    type: global___KeygenType.ValueType
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        type: global___KeygenType.ValueType = ...,
        members: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "members", b"members", "type", b"type"]) -> None: ...

global___Keygen = Keygen

@typing_extensions.final
class KeygenBlock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    KEYGENS_FIELD_NUMBER: builtins.int
    height: builtins.int
    @property
    def keygens(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Keygen]: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        keygens: collections.abc.Iterable[global___Keygen] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "keygens", b"keygens"]) -> None: ...

global___KeygenBlock = KeygenBlock
