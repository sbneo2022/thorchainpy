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
import thorchain.v1.x.thorchain.types.type_tx_out_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Status:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Status.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    incomplete: _Status.ValueType  # 0
    done: _Status.ValueType  # 1
    reverted: _Status.ValueType  # 2

class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...

incomplete: Status.ValueType  # 0
done: Status.ValueType  # 1
reverted: Status.ValueType  # 2
global___Status = Status

@typing_extensions.final
class ObservedTx(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    OUT_HASHES_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    SIGNERS_FIELD_NUMBER: builtins.int
    OBSERVED_PUB_KEY_FIELD_NUMBER: builtins.int
    KEYSIGN_MS_FIELD_NUMBER: builtins.int
    FINALISE_HEIGHT_FIELD_NUMBER: builtins.int
    AGGREGATOR_FIELD_NUMBER: builtins.int
    AGGREGATOR_TARGET_FIELD_NUMBER: builtins.int
    AGGREGATOR_TARGET_LIMIT_FIELD_NUMBER: builtins.int
    @property
    def tx(self) -> thorchain.v1.common.common_pb2.Tx: ...
    status: global___Status.ValueType
    @property
    def out_hashes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    block_height: builtins.int
    @property
    def signers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    observed_pub_key: builtins.str
    keysign_ms: builtins.int
    finalise_height: builtins.int
    aggregator: builtins.str
    aggregator_target: builtins.str
    aggregator_target_limit: builtins.str
    def __init__(
        self,
        *,
        tx: thorchain.v1.common.common_pb2.Tx | None = ...,
        status: global___Status.ValueType = ...,
        out_hashes: collections.abc.Iterable[builtins.str] | None = ...,
        block_height: builtins.int = ...,
        signers: collections.abc.Iterable[builtins.str] | None = ...,
        observed_pub_key: builtins.str = ...,
        keysign_ms: builtins.int = ...,
        finalise_height: builtins.int = ...,
        aggregator: builtins.str = ...,
        aggregator_target: builtins.str = ...,
        aggregator_target_limit: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregator", b"aggregator", "aggregator_target", b"aggregator_target", "aggregator_target_limit", b"aggregator_target_limit", "block_height", b"block_height", "finalise_height", b"finalise_height", "keysign_ms", b"keysign_ms", "observed_pub_key", b"observed_pub_key", "out_hashes", b"out_hashes", "signers", b"signers", "status", b"status", "tx", b"tx"]) -> None: ...

global___ObservedTx = ObservedTx

@typing_extensions.final
class ObservedTxVoter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_ID_FIELD_NUMBER: builtins.int
    TX_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    TXS_FIELD_NUMBER: builtins.int
    ACTIONS_FIELD_NUMBER: builtins.int
    OUT_TXS_FIELD_NUMBER: builtins.int
    FINALISED_HEIGHT_FIELD_NUMBER: builtins.int
    UPDATED_VAULT_FIELD_NUMBER: builtins.int
    REVERTED_FIELD_NUMBER: builtins.int
    OUTBOUND_HEIGHT_FIELD_NUMBER: builtins.int
    tx_id: builtins.str
    @property
    def tx(self) -> global___ObservedTx: ...
    height: builtins.int
    @property
    def txs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ObservedTx]: ...
    @property
    def actions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thorchain.v1.x.thorchain.types.type_tx_out_pb2.TxOutItem]: ...
    @property
    def out_txs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thorchain.v1.common.common_pb2.Tx]: ...
    finalised_height: builtins.int
    updated_vault: builtins.bool
    reverted: builtins.bool
    outbound_height: builtins.int
    def __init__(
        self,
        *,
        tx_id: builtins.str = ...,
        tx: global___ObservedTx | None = ...,
        height: builtins.int = ...,
        txs: collections.abc.Iterable[global___ObservedTx] | None = ...,
        actions: collections.abc.Iterable[thorchain.v1.x.thorchain.types.type_tx_out_pb2.TxOutItem] | None = ...,
        out_txs: collections.abc.Iterable[thorchain.v1.common.common_pb2.Tx] | None = ...,
        finalised_height: builtins.int = ...,
        updated_vault: builtins.bool = ...,
        reverted: builtins.bool = ...,
        outbound_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actions", b"actions", "finalised_height", b"finalised_height", "height", b"height", "out_txs", b"out_txs", "outbound_height", b"outbound_height", "reverted", b"reverted", "tx", b"tx", "tx_id", b"tx_id", "txs", b"txs", "updated_vault", b"updated_vault"]) -> None: ...

global___ObservedTxVoter = ObservedTxVoter
