"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.bank.v1beta1.query_pb2
import grpc

class QueryStub:
    """Query defines the gRPC querier service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Balance: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QueryBalanceRequest,
        cosmos.bank.v1beta1.query_pb2.QueryBalanceResponse,
    ]
    """Balance queries the balance of a single coin for a single account."""
    AllBalances: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QueryAllBalancesRequest,
        cosmos.bank.v1beta1.query_pb2.QueryAllBalancesResponse,
    ]
    """AllBalances queries the balance of all coins for a single account."""
    SpendableBalances: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesRequest,
        cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesResponse,
    ]
    """SpendableBalances queries the spenable balance of all coins for a single
    account.
    """
    TotalSupply: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyRequest,
        cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyResponse,
    ]
    """TotalSupply queries the total supply of all coins."""
    SupplyOf: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QuerySupplyOfRequest,
        cosmos.bank.v1beta1.query_pb2.QuerySupplyOfResponse,
    ]
    """SupplyOf queries the supply of a single coin."""
    Params: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QueryParamsRequest,
        cosmos.bank.v1beta1.query_pb2.QueryParamsResponse,
    ]
    """Params queries the parameters of x/bank module."""
    DenomMetadata: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataRequest,
        cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataResponse,
    ]
    """DenomsMetadata queries the client metadata of a given coin denomination."""
    DenomsMetadata: grpc.UnaryUnaryMultiCallable[
        cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataRequest,
        cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataResponse,
    ]
    """DenomsMetadata queries the client metadata for all registered coin denominations."""

class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""

    @abc.abstractmethod
    def Balance(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QueryBalanceRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QueryBalanceResponse:
        """Balance queries the balance of a single coin for a single account."""
    @abc.abstractmethod
    def AllBalances(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QueryAllBalancesRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QueryAllBalancesResponse:
        """AllBalances queries the balance of all coins for a single account."""
    @abc.abstractmethod
    def SpendableBalances(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesResponse:
        """SpendableBalances queries the spenable balance of all coins for a single
        account.
        """
    @abc.abstractmethod
    def TotalSupply(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyResponse:
        """TotalSupply queries the total supply of all coins."""
    @abc.abstractmethod
    def SupplyOf(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QuerySupplyOfRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QuerySupplyOfResponse:
        """SupplyOf queries the supply of a single coin."""
    @abc.abstractmethod
    def Params(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QueryParamsResponse:
        """Params queries the parameters of x/bank module."""
    @abc.abstractmethod
    def DenomMetadata(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataResponse:
        """DenomsMetadata queries the client metadata of a given coin denomination."""
    @abc.abstractmethod
    def DenomsMetadata(
        self,
        request: cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataResponse:
        """DenomsMetadata queries the client metadata for all registered coin denominations."""

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...