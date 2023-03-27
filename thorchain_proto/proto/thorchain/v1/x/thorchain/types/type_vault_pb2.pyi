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
import thorchain.v1.common.common_pb2
import thorchain.v1.x.thorchain.types.type_chain_contract_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _VaultType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VaultTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VaultType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UnknownVault: _VaultType.ValueType  # 0
    AsgardVault: _VaultType.ValueType  # 1
    YggdrasilVault: _VaultType.ValueType  # 2

class VaultType(_VaultType, metaclass=_VaultTypeEnumTypeWrapper): ...

UnknownVault: VaultType.ValueType  # 0
AsgardVault: VaultType.ValueType  # 1
YggdrasilVault: VaultType.ValueType  # 2
global___VaultType = VaultType

class _VaultStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VaultStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VaultStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    InactiveVault: _VaultStatus.ValueType  # 0
    ActiveVault: _VaultStatus.ValueType  # 1
    RetiringVault: _VaultStatus.ValueType  # 2
    InitVault: _VaultStatus.ValueType  # 3

class VaultStatus(_VaultStatus, metaclass=_VaultStatusEnumTypeWrapper): ...

InactiveVault: VaultStatus.ValueType  # 0
ActiveVault: VaultStatus.ValueType  # 1
RetiringVault: VaultStatus.ValueType  # 2
InitVault: VaultStatus.ValueType  # 3
global___VaultStatus = VaultStatus

@typing_extensions.final
class Vault(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    PUB_KEY_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    STATUS_SINCE_FIELD_NUMBER: builtins.int
    MEMBERSHIP_FIELD_NUMBER: builtins.int
    CHAINS_FIELD_NUMBER: builtins.int
    INBOUND_TX_COUNT_FIELD_NUMBER: builtins.int
    OUTBOUND_TX_COUNT_FIELD_NUMBER: builtins.int
    PENDING_TX_BLOCK_HEIGHTS_FIELD_NUMBER: builtins.int
    ROUTERS_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    pub_key: builtins.str
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thorchain.v1.common.common_pb2.Coin]: ...
    type: global___VaultType.ValueType
    status: global___VaultStatus.ValueType
    status_since: builtins.int
    @property
    def membership(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def chains(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    inbound_tx_count: builtins.int
    outbound_tx_count: builtins.int
    @property
    def pending_tx_block_heights(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def routers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thorchain.v1.x.thorchain.types.type_chain_contract_pb2.ChainContract]: ...
    def __init__(
        self,
        *,
        block_height: builtins.int = ...,
        pub_key: builtins.str = ...,
        coins: collections.abc.Iterable[thorchain.v1.common.common_pb2.Coin] | None = ...,
        type: global___VaultType.ValueType = ...,
        status: global___VaultStatus.ValueType = ...,
        status_since: builtins.int = ...,
        membership: collections.abc.Iterable[builtins.str] | None = ...,
        chains: collections.abc.Iterable[builtins.str] | None = ...,
        inbound_tx_count: builtins.int = ...,
        outbound_tx_count: builtins.int = ...,
        pending_tx_block_heights: collections.abc.Iterable[builtins.int] | None = ...,
        routers: collections.abc.Iterable[thorchain.v1.x.thorchain.types.type_chain_contract_pb2.ChainContract] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height", b"block_height", "chains", b"chains", "coins", b"coins", "inbound_tx_count", b"inbound_tx_count", "membership", b"membership", "outbound_tx_count", b"outbound_tx_count", "pending_tx_block_heights", b"pending_tx_block_heights", "pub_key", b"pub_key", "routers", b"routers", "status", b"status", "status_since", b"status_since", "type", b"type"]) -> None: ...

global___Vault = Vault
