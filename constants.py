from typing import Final, Dict

# Network identifier constants
MAINNET: Final[str] = "mainnet"
TESTNET: Final[str] = "testnet"

# Unit conversion factors
SATOSHIS_PER_BTC: Final[int] = 100_000_000
WEI_PER_ETH: Final[int] = 10**18

# Supported asset symbols
ASSET_BTC: Final[str] = "BTC"
ASSET_ETH: Final[str] = "ETH"
ASSET_USDT: Final[str] = "USDT"

# API request configuration
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Standardized path keys
CONFIG_PATH: Final[str] = "/etc/wallet/config.json"
LOG_DIR: Final[str] = "/var/log/wallet-utility-13/"

# Mapping of chain IDs to native currency
CHAIN_NATIVE_MAP: Final[Dict[int, str]] = {
    1: ASSET_ETH,
    56: "BNB",
    137: "MATIC"
}

# Decimal precision settings
DEFAULT_PRECISION: Final[int] = 8
FEE_PRECISION: Final[int] = 18