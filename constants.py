"""Cryptocurrency network constants and blockchain configurations."""

from dataclasses import dataclass
from enum import Enum


class NetworkType(Enum):
    MAINNET = "mainnet"
    TESTNET = "testnet"
    DEVNET = "devnet"


@dataclass(frozen=True)
class ChainConfig:
    chain_id: int
    name: str
    symbol: str
    decimals: int
    default_rpc: str
    explorer_url: str


# Chain Configurations
ETHEREUM_MAINNET = ChainConfig(
    chain_id=1,
    name="Ethereum Mainnet",
    symbol="ETH",
    decimals=18,
    default_rpc="https://eth.llamarpc.com",
    explorer_url="https://etherscan.io",
)

POLYGON_MAINNET = ChainConfig(
    chain_id=137,
    name="Polygon Mainnet",
    symbol="POL",
    decimals=18,
    default_rpc="https://polygon-rpc.com",
    explorer_url="https://polygonscan.com",
)

ARBITRUM_ONE = ChainConfig(
    chain_id=42161,
    name="Arbitrum One",
    symbol="ETH",
    decimals=18,
    default_rpc="https://arb1.arbitrum.io/rpc",
    explorer_url="https://arbiscan.io",
)

SUPPORTED_CHAINS = {
    ETHEREUM_MAINNET.chain_id: ETHEREUM_MAINNET,
    POLYGON_MAINNET.chain_id: POLYGON_MAINNET,
    ARBITRUM_ONE.chain_id: ARBITRUM_ONE,
}

# Transaction Default Limits
DEFAULT_GAS_LIMIT_NATIVE = 21_000
DEFAULT_GAS_LIMIT_ERC20 = 65_000
GWEI_TO_WEI_FACTOR = 10**9
ETH_TO_WEI_FACTOR = 10**18

# Standard ERC20 Minimal ABI Definitions
ERC20_MINIMAL_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "type": "function",
    },
]
