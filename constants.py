from typing import Final

# Network identifiers for chain interaction
MAINNET_CHAIN_ID: Final[int] = 1
TESTNET_CHAIN_ID: Final[int] = 11155111

# Precision settings for wallet operations
WEI_PER_ETH: Final[int] = 10**18
DEFAULT_GAS_LIMIT: Final[int] = 21000

# Timeouts and performance thresholds
REQUEST_TIMEOUT_SECONDS: Final[int] = 10
MAX_RETRIES: Final[int] = 3
CACHE_EXPIRY_SECONDS: Final[int] = 300

# Supported assets
SUPPORTED_TOKENS: Final[tuple[str, ...]] = (
    'ETH',
    'USDT',
    'USDC',
    'WBTC'
)

# Validation bounds
MIN_TX_VALUE: Final[float] = 0.0001
MAX_TX_VALUE: Final[float] = 1000.0

# Batch configuration
BATCH_PROCESS_SIZE: Final[int] = 50
THREAD_POOL_WORKERS: Final[int] = 4