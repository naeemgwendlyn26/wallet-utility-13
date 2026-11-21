from typing import Dict, Final

# Crypto currency network identifiers and precision settings
NETWORK_PRECISION: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "USDC": 6,
    "SOL": 9
}

# Standardized API endpoint suffixes
ENDPOINT_MAP: Final[Dict[str, str]] = {
    "v1": "/api/v1/public",
    "v2": "/api/v2/private",
    "stream": "/ws/v1/market"
}

# Transaction status constants
STATUS_PENDING: Final[str] = "pending"
STATUS_CONFIRMED: Final[str] = "confirmed"
STATUS_FAILED: Final[str] = "failed"

# Default network timeout in seconds
DEFAULT_TIMEOUT: Final[int] = 30

def get_precision(symbol: str) -> int:
    """Return decimal precision for a given ticker symbol."""
    return NETWORK_PRECISION.get(symbol.upper(), 8)

def is_valid_status(status: str) -> bool:
    """Validate if the status string matches expected crypto states."""
    valid_statuses = [STATUS_PENDING, STATUS_CONFIRMED, STATUS_FAILED]
    return status.lower() in valid_statuses