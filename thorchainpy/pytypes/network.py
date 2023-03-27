"""
The network class allows the user to defines the network the sdk interface should connect to.

There are some default values set for devnet, testnet, mainet and localnet, but the user cna also define its own
network by setting the values of the Network data class.

"""
import dataclasses
import enum
import os
from typing import Dict, List, Optional


class NetworkType(enum.Enum):
    LOCALNET = "localnet"
    DEVNET = "devnet"
    TESTNET = "testnet"
    MAINNET = "mainnet"


@dataclasses.dataclass
class Network:
    lcd_endpoint: str
    grpc_endpoint: str
    tendermint_rpc_endpoint: str
    chain_id: str
    env: str = "custom"

    @property
    def is_insecure(self) -> bool:
        return not ("https" in self.tendermint_rpc_endpoint)

    @classmethod
    def localnet(cls) -> "Network":
        return cls(
            lcd_endpoint=f'http://localhost:1317',
            grpc_endpoint=f'localhost:9091',
            tendermint_rpc_endpoint=f'http://localhost:26657',
            chain_id=f'thorchain',
            env=NetworkType.LOCALNET.value,
        )

    @classmethod
    def devnet(cls) -> "Network":
        """
        **NOT IMPLEMENTED YET**
        """
        raise NotImplementedError

    @classmethod
    def testnet(cls) -> "Network":
        return cls(
            lcd_endpoint=f'http://testnet.midgard.thorchain.info:1317',
            grpc_endpoint=f'testnet.midgard.thorchain.info:9090',
            tendermint_rpc_endpoint=f'http://testnet.midgard.thorchain.info:26657	',
            chain_id=f'thorchain',
            env=NetworkType.TESTNET.value,
        )

    @classmethod
    def mainnet(cls) -> "Network":
        return cls(
            lcd_endpoint=f'http://thornode:1317/thorchain',
            grpc_endpoint=f'midgard.thorswap.net:9090',
            tendermint_rpc_endpoint=f'http://thornode:26657/websocket',
            chain_id=f'thorchain',
            env=NetworkType.MAINNET.value,
        )

    def string(self) -> str:
        """
        Returns the current environment the network was initialized with. Will return `custom` if a custom network
        was created

        Returns:
            str: The name of the current environment.
        """
        return self.env
