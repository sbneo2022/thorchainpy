class ThorchainError(Exception):
    pass


class SimulationError(ThorchainError):
    pass


class TxError(ThorchainError):
    pass


class QueryError(ThorchainError):
    pass
