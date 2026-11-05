class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class ConnectionError(WalletError):
    """Raised when RPC or node connectivity fails."""
    pass

class ValidationError(WalletError):
    """Raised when address or transaction data is invalid."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is too low for operation."""
    pass

class SecurityError(WalletError):
    """Raised when signing or key operations fail."""
    pass

class RateLimitError(WalletError):
    """Raised when API requests exceed threshold."""
    pass

def handle_exception(e: Exception) -> None:
    """Centralized error classification for logging."""
    if isinstance(e, WalletError):
        print(f"Wallet operational error: {e}")
    else:
        print(f"Unexpected system failure: {e}")