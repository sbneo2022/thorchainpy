"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tendermint.abci.types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TxResponse(google.protobuf.message.Message):
    """TxResponse defines a structure containing relevant tx data and metadata. The
    tags are stringified and the log is JSON decoded.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    TXHASH_FIELD_NUMBER: builtins.int
    CODESPACE_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    RAW_LOG_FIELD_NUMBER: builtins.int
    LOGS_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    GAS_WANTED_FIELD_NUMBER: builtins.int
    GAS_USED_FIELD_NUMBER: builtins.int
    TX_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    EVENTS_FIELD_NUMBER: builtins.int
    height: builtins.int
    """The block height"""
    txhash: builtins.str
    """The transaction hash."""
    codespace: builtins.str
    """Namespace for the Code"""
    code: builtins.int
    """Response code."""
    data: builtins.str
    """Result bytes, if any."""
    raw_log: builtins.str
    """The output of the application's logger (raw string). May be
    non-deterministic.
    """
    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ABCIMessageLog]:
        """The output of the application's logger (typed). May be non-deterministic."""
    info: builtins.str
    """Additional information. May be non-deterministic."""
    gas_wanted: builtins.int
    """Amount of gas requested for transaction."""
    gas_used: builtins.int
    """Amount of gas consumed by transaction."""
    @property
    def tx(self) -> google.protobuf.any_pb2.Any:
        """The request transaction bytes."""
    timestamp: builtins.str
    """Time of the previous block. For heights > 1, it's the weighted median of
    the timestamps of the valid votes in the block.LastCommit. For height == 1,
    it's genesis time.
    """
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tendermint.abci.types_pb2.Event]:
        """Events defines all the events emitted by processing a transaction. Note,
        these events include those emitted by processing all the messages and those
        emitted from the ante handler. Whereas Logs contains the events, with
        additional metadata, emitted only by processing the messages.

        Since: cosmos-sdk 0.42.11, 0.44.5, 0.45
        """
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        txhash: builtins.str = ...,
        codespace: builtins.str = ...,
        code: builtins.int = ...,
        data: builtins.str = ...,
        raw_log: builtins.str = ...,
        logs: collections.abc.Iterable[global___ABCIMessageLog] | None = ...,
        info: builtins.str = ...,
        gas_wanted: builtins.int = ...,
        gas_used: builtins.int = ...,
        tx: google.protobuf.any_pb2.Any | None = ...,
        timestamp: builtins.str = ...,
        events: collections.abc.Iterable[tendermint.abci.types_pb2.Event] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "codespace", b"codespace", "data", b"data", "events", b"events", "gas_used", b"gas_used", "gas_wanted", b"gas_wanted", "height", b"height", "info", b"info", "logs", b"logs", "raw_log", b"raw_log", "timestamp", b"timestamp", "tx", b"tx", "txhash", b"txhash"]) -> None: ...

global___TxResponse = TxResponse

@typing_extensions.final
class ABCIMessageLog(google.protobuf.message.Message):
    """ABCIMessageLog defines a structure containing an indexed tx ABCI message log."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MSG_INDEX_FIELD_NUMBER: builtins.int
    LOG_FIELD_NUMBER: builtins.int
    EVENTS_FIELD_NUMBER: builtins.int
    msg_index: builtins.int
    log: builtins.str
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StringEvent]:
        """Events contains a slice of Event objects that were emitted during some
        execution.
        """
    def __init__(
        self,
        *,
        msg_index: builtins.int = ...,
        log: builtins.str = ...,
        events: collections.abc.Iterable[global___StringEvent] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["events", b"events", "log", b"log", "msg_index", b"msg_index"]) -> None: ...

global___ABCIMessageLog = ABCIMessageLog

@typing_extensions.final
class StringEvent(google.protobuf.message.Message):
    """StringEvent defines en Event object wrapper where all the attributes
    contain key/value pairs that are strings instead of raw bytes.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    type: builtins.str
    @property
    def attributes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Attribute]: ...
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        attributes: collections.abc.Iterable[global___Attribute] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes", b"attributes", "type", b"type"]) -> None: ...

global___StringEvent = StringEvent

@typing_extensions.final
class Attribute(google.protobuf.message.Message):
    """Attribute defines an attribute wrapper where the key and value are
    strings instead of raw bytes.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

global___Attribute = Attribute

@typing_extensions.final
class GasInfo(google.protobuf.message.Message):
    """GasInfo defines tx execution gas context."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GAS_WANTED_FIELD_NUMBER: builtins.int
    GAS_USED_FIELD_NUMBER: builtins.int
    gas_wanted: builtins.int
    """GasWanted is the maximum units of work we allow this tx to perform."""
    gas_used: builtins.int
    """GasUsed is the amount of gas actually consumed."""
    def __init__(
        self,
        *,
        gas_wanted: builtins.int = ...,
        gas_used: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gas_used", b"gas_used", "gas_wanted", b"gas_wanted"]) -> None: ...

global___GasInfo = GasInfo

@typing_extensions.final
class Result(google.protobuf.message.Message):
    """Result is the union of ResponseFormat and ResponseCheckTx."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    LOG_FIELD_NUMBER: builtins.int
    EVENTS_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """Data is any data returned from message or handler execution. It MUST be
    length prefixed in order to separate data from multiple message executions.
    """
    log: builtins.str
    """Log contains the log information from message or handler execution."""
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tendermint.abci.types_pb2.Event]:
        """Events contains a slice of Event objects that were emitted during message
        or handler execution.
        """
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
        log: builtins.str = ...,
        events: collections.abc.Iterable[tendermint.abci.types_pb2.Event] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "events", b"events", "log", b"log"]) -> None: ...

global___Result = Result

@typing_extensions.final
class SimulationResponse(google.protobuf.message.Message):
    """SimulationResponse defines the response generated when a transaction is
    successfully simulated.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GAS_INFO_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def gas_info(self) -> global___GasInfo: ...
    @property
    def result(self) -> global___Result: ...
    def __init__(
        self,
        *,
        gas_info: global___GasInfo | None = ...,
        result: global___Result | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gas_info", b"gas_info", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gas_info", b"gas_info", "result", b"result"]) -> None: ...

global___SimulationResponse = SimulationResponse

@typing_extensions.final
class MsgData(google.protobuf.message.Message):
    """MsgData defines the data returned in a Result object during message
    execution.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MSG_TYPE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    msg_type: builtins.str
    data: builtins.bytes
    def __init__(
        self,
        *,
        msg_type: builtins.str = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "msg_type", b"msg_type"]) -> None: ...

global___MsgData = MsgData

@typing_extensions.final
class TxMsgData(google.protobuf.message.Message):
    """TxMsgData defines a list of MsgData. A transaction will have a MsgData object
    for each message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MsgData]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[global___MsgData] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___TxMsgData = TxMsgData

@typing_extensions.final
class SearchTxsResult(google.protobuf.message.Message):
    """SearchTxsResult defines a structure for querying txs pageable"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    PAGE_NUMBER_FIELD_NUMBER: builtins.int
    PAGE_TOTAL_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    TXS_FIELD_NUMBER: builtins.int
    total_count: builtins.int
    """Count of all txs"""
    count: builtins.int
    """Count of txs in current page"""
    page_number: builtins.int
    """Index of current page, start from 1"""
    page_total: builtins.int
    """Count of total pages"""
    limit: builtins.int
    """Max count txs per page"""
    @property
    def txs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TxResponse]:
        """List of txs in current page"""
    def __init__(
        self,
        *,
        total_count: builtins.int = ...,
        count: builtins.int = ...,
        page_number: builtins.int = ...,
        page_total: builtins.int = ...,
        limit: builtins.int = ...,
        txs: collections.abc.Iterable[global___TxResponse] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["count", b"count", "limit", b"limit", "page_number", b"page_number", "page_total", b"page_total", "total_count", b"total_count", "txs", b"txs"]) -> None: ...

global___SearchTxsResult = SearchTxsResult
