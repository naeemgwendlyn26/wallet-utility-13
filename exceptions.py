import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class WalletError(Exception):
    """Base class for wallet utility exceptions."""
    def __init__(self, message: str, error_code: str = "WALLET_ERROR", details: Optional[Dict[str, Any]] = None) -> None:
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for logging or API responses."""
        return {
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details
        }

class InvalidAddressError(WalletError):
    """Raised for invalid cryptocurrency wallet addresses."""
    def __init__(self, address: str) -> None:
        message = f"Invalid wallet address format: {address}"
        super().__init__(message, "INVALID_ADDRESS", {"address": address})

class InsufficientBalanceError(WalletError):
    """Raised when account balance is insufficient."""
    def __init__(self, required: float, available: float, asset: str = "ETH") -> None:
        message = f"Insufficient {asset} balance. Required {required}, have {available}"
        super().__init__(message, "INSUFFICIENT_BALANCE", {
            "required": required,
            "available": available,
            "asset": asset
        })

class NetworkError(WalletError):
    """Raised for blockchain network connectivity problems."""
    def __init__(self, network: str, details: str) -> None:
        message = f"Network error on {network}: {details}"
        super().__init__(message, "NETWORK_ERROR", {"network": network, "details": details})

class TransactionError(WalletError):
    """Raised when transaction processing fails."""
    def __init__(self, reason: str, tx_hash: Optional[str] = None) -> None:
        message = f"Transaction failed: {reason}"
        details = {"reason": reason}
        if tx_hash:
            details["tx_hash"] = tx_hash
        super().__init__(message, "TRANSACTION_ERROR", details)

class PrivateKeyError(WalletError):
    """Raised for issues with private keys."""
    def __init__(self, reason: str = "Invalid or missing private key") -> None:
        super().__init__(reason, "PRIVATE_KEY_ERROR")

class GasError(WalletError):
    """Raised for gas related issues in transactions."""
    def __init__(self, current_price: float, max_allowed: float) -> None:
        message = f"Gas price {current_price} exceeds max allowed {max_allowed}"
        super().__init__(message, "GAS_ERROR", {"current": current_price, "max": max_allowed})

class RateLimitError(WalletError):
    """Raised when rate limits are hit on API calls."""
    def __init__(self, retry_after: int) -> None:
        message = f"Rate limit reached. Retry after {retry_after} seconds"
        super().__init__(message, "RATE_LIMIT_ERROR", {"retry_after": retry_after})

def log_and_raise(error: WalletError) -> None:
    """Log the error and raise it."""
    logger.error(f"Wallet error: {error.to_dict()}")
    raise error