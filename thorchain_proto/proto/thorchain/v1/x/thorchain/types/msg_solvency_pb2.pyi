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
import thorchain.v1.common.common_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgSolvency(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CHAIN_FIELD_NUMBER: builtins.int
    PUB_KEY_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    id: builtins.str
    chain: builtins.str
    pub_key: builtins.str
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thorchain.v1.common.common_pb2.Coin]: ...
    height: builtins.int
    signer: builtins.bytes
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        chain: builtins.str = ...,
        pub_key: builtins.str = ...,
        coins: collections.abc.Iterable[thorchain.v1.common.common_pb2.Coin] | None = ...,
        height: builtins.int = ...,
        signer: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain", b"chain", "coins", b"coins", "height", b"height", "id", b"id", "pub_key", b"pub_key", "signer", b"signer"]) -> None: ...

global___MsgSolvency = MsgSolvency
