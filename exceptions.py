class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is too low."""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when RPC or network calls fail."""
    pass

class TransactionValidationError(WalletError):
    """Raised when transaction data is malformed."""
    pass

class InvalidAddressError(WalletError):
    """Raised when wallet address format is invalid."""
    pass

def handle_crypto_error(err: Exception) -> str:
    """Format errors for logging and UI display."""
    if isinstance(err, InsufficientFundsError):
        return "insufficient funds for operation"
    if isinstance(err, InvalidAddressError):
        return "provided address is not valid"
    if isinstance(err, NetworkTimeoutError):
        return "network connection issue detected"
    return f"unexpected error: {str(err)}"