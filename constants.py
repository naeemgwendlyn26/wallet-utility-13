from typing import Final, Dict

# Configuration constants for crypto wallet operations
BLOCKCHAIN_NETWORKS: Final[list[str]] = ["ethereum", "bitcoin", "solana", "polygon"]

# Default transaction fee limits in Gwei or Satoshis
DEFAULT_GAS_LIMIT: Final[int] = 21000
MAX_RETRY_ATTEMPTS: Final[int] = 3

# Currency precision mapping for wallet UI display
CURRENCY_PRECISION: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "SOL": 9,
    "USDC": 6
}

# Wallet connection status codes
STATUS_CONNECTED: Final[str] = "CONNECTED"
STATUS_DISCONNECTED: Final[str] = "DISCONNECTED"
STATUS_SYNCING: Final[str] = "SYNCING"

def get_precision(symbol: str) -> int:
    """Return the decimal precision for a given currency symbol."""
    return CURRENCY_PRECISION.get(symbol.upper(), 8)

# API Timeout configuration
REQUEST_TIMEOUT_SECONDS: Final[float] = 30.0
API_BASE_URL: Final[str] = "https://api.wallet-utility-13.io/v1"