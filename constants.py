from typing import Final, Dict

# Network identifiers for blockchain integration
MAINNET: Final[str] = "mainnet"
TESTNET: Final[str] = "testnet"

# Precision settings for crypto balance calculations
SATOSHI_UNIT: Final[int] = 10**8
WEI_UNIT: Final[int] = 10**18

# Supported cryptocurrency asset mapping
ASSET_MAP: Dict[str, str] = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana"
}

# Rate limit configuration for API interaction
API_TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Regex pattern for wallet address validation
WALLET_ADDRESS_REGEX: Final[str] = r"^[a-zA-Z0-9]{26,42}$"

# Transaction status codes
STATUS_PENDING: Final[int] = 0
STATUS_CONFIRMED: Final[int] = 1
STATUS_FAILED: Final[int] = -1