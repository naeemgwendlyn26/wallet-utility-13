class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when transaction exceeds available funds."""
    pass

class InvalidAddressError(WalletError):
    """Raised when the provided wallet address format is invalid."""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when blockchain RPC calls time out."""
    pass

class TransactionSigningError(WalletError):
    """Raised when cryptographic signature creation fails."""
    pass

class RateLimitExceededError(WalletError):
    """Raised when API request frequency limits are hit."""
    pass

def handle_exception(e: Exception) -> str:
    """Format exception messages for consistent logging."""
    if isinstance(e, WalletError):
        return f"[WalletUtility] {type(e).__name__}: {str(e)}"
    return f"[WalletUtility] UnexpectedError: {str(e)}"