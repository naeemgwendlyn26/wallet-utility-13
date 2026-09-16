class WalletError(Exception):
    """Base exception for all wallet-utility-13 operations."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when transaction amount exceeds available balance."""
    pass

class InvalidAddressError(WalletError):
    """Raised when the provided cryptocurrency address format is invalid."""
    pass

class NetworkConnectionError(WalletError):
    """Raised when RPC or network requests fail."""
    pass

class TransactionSigningError(WalletError):
    """Raised when private key signing operations fail."""
    pass

class ConfigurationError(WalletError):
    """Raised when environment variables or config files are missing."""
    pass

def handle_exception(e: Exception) -> str:
    """Format exception message for logger output."""
    if isinstance(e, WalletError):
        return f"[WalletError] {e}"
    return f"[UnexpectedError] {type(e).__name__}: {str(e)}"