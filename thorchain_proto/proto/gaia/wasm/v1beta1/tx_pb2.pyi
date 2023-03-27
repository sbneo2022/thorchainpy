"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
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
class MsgExecuteContract(google.protobuf.message.Message):
    """MsgExecuteContract represents a message to
    submits the given message data to a smart contract.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    CONTRACT_FIELD_NUMBER: builtins.int
    EXECUTE_MSG_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    sender: builtins.str
    """Sender is the that actor that signed the messages"""
    contract: builtins.str
    """Contract is the address of the smart contract"""
    execute_msg: builtins.bytes
    """ExecuteMsg json encoded message to be passed to the contract"""
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """Coins that are transferred to the contract on execution"""
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        contract: builtins.str = ...,
        execute_msg: builtins.bytes = ...,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins", "contract", b"contract", "execute_msg", b"execute_msg", "sender", b"sender"]) -> None: ...

global___MsgExecuteContract = MsgExecuteContract

@typing_extensions.final
class MsgExecuteContractResponse(google.protobuf.message.Message):
    """MsgExecuteContractResponse defines the Msg/ExecuteContract response type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """Data contains base64-encoded bytes to returned from the contract"""
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___MsgExecuteContractResponse = MsgExecuteContractResponse
