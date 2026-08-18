from typing import Final

# Constant values used throughout the wallet utility

API_URL: Final[str] = "https://api.crypto.com/v1"
# The base URL for the crypto API

MAX_TRANSACTION_LIMIT: Final[int] = 10000
# The maximum number of transactions allowed in a single operation

SUPPORTED_CURRENCIES: Final[set] = {"BTC", "ETH", "LTC"}
# A set of currencies supported by the wallet utility

DEFAULT_FEE: Final[float] = 0.001
# Default transaction fee as a percentage

MINIMUM_BALANCE: Final[float] = 0.01
# The minimum balance required in the wallet

TRANSACTION_STATUS: Final[dict] = {
    "PENDING": "Transaction is in progress",
    "COMPLETED": "Transaction has been completed",
    "FAILED": "Transaction has failed"
}
# Dictionary defining possible transaction statuses