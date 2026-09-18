class WalletError(Exception):
    """Base exception for all wallet operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is below transaction cost."""
    def __init__(self, required, actual):
        super().__init__(f"Required {required}, but found {actual}")

class InvalidAddressError(WalletError):
    """Raised when a blockchain address format is malformed."""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when blockchain RPC requests exceed timeout."""
    pass

class SigningError(WalletError):
    """Raised when cryptographic signature generation fails."""
    pass

class RateLimitError(WalletError):
    """Raised when hitting node provider rate limits."""
    pass
