"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.gov.v1beta1.gov_pb2
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
class QueryProposalRequest(google.protobuf.message.Message):
    """QueryProposalRequest is the request type for the Query/Proposal RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id"]) -> None: ...

global___QueryProposalRequest = QueryProposalRequest

@typing_extensions.final
class QueryProposalResponse(google.protobuf.message.Message):
    """QueryProposalResponse is the response type for the Query/Proposal RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_FIELD_NUMBER: builtins.int
    @property
    def proposal(self) -> cosmos.gov.v1beta1.gov_pb2.Proposal: ...
    def __init__(
        self,
        *,
        proposal: cosmos.gov.v1beta1.gov_pb2.Proposal | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["proposal", b"proposal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal", b"proposal"]) -> None: ...

global___QueryProposalResponse = QueryProposalResponse

@typing_extensions.final
class QueryProposalsRequest(google.protobuf.message.Message):
    """QueryProposalsRequest is the request type for the Query/Proposals RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_STATUS_FIELD_NUMBER: builtins.int
    VOTER_FIELD_NUMBER: builtins.int
    DEPOSITOR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    proposal_status: cosmos.gov.v1beta1.gov_pb2.ProposalStatus.ValueType
    """proposal_status defines the status of the proposals."""
    voter: builtins.str
    """voter defines the voter address for the proposals."""
    depositor: builtins.str
    """depositor defines the deposit addresses from the proposals."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
    def __init__(
        self,
        *,
        proposal_status: cosmos.gov.v1beta1.gov_pb2.ProposalStatus.ValueType = ...,
        voter: builtins.str = ...,
        depositor: builtins.str = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["depositor", b"depositor", "pagination", b"pagination", "proposal_status", b"proposal_status", "voter", b"voter"]) -> None: ...

global___QueryProposalsRequest = QueryProposalsRequest

@typing_extensions.final
class QueryProposalsResponse(google.protobuf.message.Message):
    """QueryProposalsResponse is the response type for the Query/Proposals RPC
    method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSALS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def proposals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Proposal]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        proposals: collections.abc.Iterable[cosmos.gov.v1beta1.gov_pb2.Proposal] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "proposals", b"proposals"]) -> None: ...

global___QueryProposalsResponse = QueryProposalsResponse

@typing_extensions.final
class QueryVoteRequest(google.protobuf.message.Message):
    """QueryVoteRequest is the request type for the Query/Vote RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    VOTER_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    voter: builtins.str
    """voter defines the oter address for the proposals."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        voter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id", "voter", b"voter"]) -> None: ...

global___QueryVoteRequest = QueryVoteRequest

@typing_extensions.final
class QueryVoteResponse(google.protobuf.message.Message):
    """QueryVoteResponse is the response type for the Query/Vote RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTE_FIELD_NUMBER: builtins.int
    @property
    def vote(self) -> cosmos.gov.v1beta1.gov_pb2.Vote:
        """vote defined the queried vote."""
    def __init__(
        self,
        *,
        vote: cosmos.gov.v1beta1.gov_pb2.Vote | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["vote", b"vote"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["vote", b"vote"]) -> None: ...

global___QueryVoteResponse = QueryVoteResponse

@typing_extensions.final
class QueryVotesRequest(google.protobuf.message.Message):
    """QueryVotesRequest is the request type for the Query/Votes RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "proposal_id", b"proposal_id"]) -> None: ...

global___QueryVotesRequest = QueryVotesRequest

@typing_extensions.final
class QueryVotesResponse(google.protobuf.message.Message):
    """QueryVotesResponse is the response type for the Query/Votes RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def votes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Vote]:
        """votes defined the queried votes."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        votes: collections.abc.Iterable[cosmos.gov.v1beta1.gov_pb2.Vote] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "votes", b"votes"]) -> None: ...

global___QueryVotesResponse = QueryVotesResponse

@typing_extensions.final
class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_TYPE_FIELD_NUMBER: builtins.int
    params_type: builtins.str
    """params_type defines which parameters to query for, can be one of "voting",
    "tallying" or "deposit".
    """
    def __init__(
        self,
        *,
        params_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["params_type", b"params_type"]) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

@typing_extensions.final
class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTING_PARAMS_FIELD_NUMBER: builtins.int
    DEPOSIT_PARAMS_FIELD_NUMBER: builtins.int
    TALLY_PARAMS_FIELD_NUMBER: builtins.int
    @property
    def voting_params(self) -> cosmos.gov.v1beta1.gov_pb2.VotingParams:
        """voting_params defines the parameters related to voting."""
    @property
    def deposit_params(self) -> cosmos.gov.v1beta1.gov_pb2.DepositParams:
        """deposit_params defines the parameters related to deposit."""
    @property
    def tally_params(self) -> cosmos.gov.v1beta1.gov_pb2.TallyParams:
        """tally_params defines the parameters related to tally."""
    def __init__(
        self,
        *,
        voting_params: cosmos.gov.v1beta1.gov_pb2.VotingParams | None = ...,
        deposit_params: cosmos.gov.v1beta1.gov_pb2.DepositParams | None = ...,
        tally_params: cosmos.gov.v1beta1.gov_pb2.TallyParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deposit_params", b"deposit_params", "tally_params", b"tally_params", "voting_params", b"voting_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deposit_params", b"deposit_params", "tally_params", b"tally_params", "voting_params", b"voting_params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing_extensions.final
class QueryDepositRequest(google.protobuf.message.Message):
    """QueryDepositRequest is the request type for the Query/Deposit RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    DEPOSITOR_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    depositor: builtins.str
    """depositor defines the deposit addresses from the proposals."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        depositor: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["depositor", b"depositor", "proposal_id", b"proposal_id"]) -> None: ...

global___QueryDepositRequest = QueryDepositRequest

@typing_extensions.final
class QueryDepositResponse(google.protobuf.message.Message):
    """QueryDepositResponse is the response type for the Query/Deposit RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSIT_FIELD_NUMBER: builtins.int
    @property
    def deposit(self) -> cosmos.gov.v1beta1.gov_pb2.Deposit:
        """deposit defines the requested deposit."""
    def __init__(
        self,
        *,
        deposit: cosmos.gov.v1beta1.gov_pb2.Deposit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deposit", b"deposit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deposit", b"deposit"]) -> None: ...

global___QueryDepositResponse = QueryDepositResponse

@typing_extensions.final
class QueryDepositsRequest(google.protobuf.message.Message):
    """QueryDepositsRequest is the request type for the Query/Deposits RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "proposal_id", b"proposal_id"]) -> None: ...

global___QueryDepositsRequest = QueryDepositsRequest

@typing_extensions.final
class QueryDepositsResponse(google.protobuf.message.Message):
    """QueryDepositsResponse is the response type for the Query/Deposits RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPOSITS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def deposits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Deposit]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        deposits: collections.abc.Iterable[cosmos.gov.v1beta1.gov_pb2.Deposit] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deposits", b"deposits", "pagination", b"pagination"]) -> None: ...

global___QueryDepositsResponse = QueryDepositsResponse

@typing_extensions.final
class QueryTallyResultRequest(google.protobuf.message.Message):
    """QueryTallyResultRequest is the request type for the Query/Tally RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id"]) -> None: ...

global___QueryTallyResultRequest = QueryTallyResultRequest

@typing_extensions.final
class QueryTallyResultResponse(google.protobuf.message.Message):
    """QueryTallyResultResponse is the response type for the Query/Tally RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TALLY_FIELD_NUMBER: builtins.int
    @property
    def tally(self) -> cosmos.gov.v1beta1.gov_pb2.TallyResult:
        """tally defines the requested tally."""
    def __init__(
        self,
        *,
        tally: cosmos.gov.v1beta1.gov_pb2.TallyResult | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tally", b"tally"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tally", b"tally"]) -> None: ...

global___QueryTallyResultResponse = QueryTallyResultResponse