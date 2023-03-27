import sys

try:
    if sys.version_info >= (3, 8):
        from importlib_metadata import version

        __version__ = version(__package__ or __name__)
    else:
        import pkg_resources

        __version__ = pkg_resources.get_distribution(
            __package__ or __name__).version
except BaseException:
    pass

import google.protobuf.message

ProtobufMessage = google.protobuf.message.Message

import thorchainpy.exceptions  # noqa
import thorchainpy.pytypes  # noqa
from thorchainpy.grpc_client import GrpcClient  # noqa
from thorchainpy.pytypes import (  # noqa
    Coin,
    Direction,
    Network,
    NetworkType,
    PoolAsset,
    Side,
    TxConfig,
    TxType,
)
from thorchainpy.sdk import Sdk  # noqa
from thorchainpy.tx import Transaction  # noqa
from thorchainpy.wallet import Address, PrivateKey, PublicKey  # noqa
