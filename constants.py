import sys
from enum import Enum
from typing import Final, Dict

# Network identifiers for chain selection
NETWORK_MAINNET: Final[str] = "mainnet"
NETWORK_TESTNET: Final[str] = "testnet"

# Optimization: pre-computed byte lengths to avoid repeated calculations
ADDR_BYTE_LEN: Final[int] = 20
TX_HASH_LEN: Final[int] = 32

# Cache dictionary for frequently accessed currency decimals
CURRENCY_DECIMALS: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "USDC": 6
}

# Configuration constraints for performance tuning
MAX_RETRIES: Final[int] = 3
CONNECTION_TIMEOUT: Final[float] = 5.0
CACHE_TTL_SECONDS: Final[int] = 300

class ChainType(Enum):
    """Supported blockchain architectures."""
    EVM = "evm"
    UTXO = "utxo"
    SOLANA = "solana"

# String encoding standards
ENCODING_UTF8: Final[str] = "utf-8"
DEFAULT_GAS_LIMIT: Final[int] = 21000