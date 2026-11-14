class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when transaction amount exceeds balance."""
    def __init__(self, required, available):
        super().__init__(f"Required {required}, but only {available} available.")
        self.required = required
        self.available = available

class NetworkConnectionError(WalletError):
    """Raised when unable to reach crypto node."""
    pass

class ValidationError(WalletError):
    """Raised for malformed addresses or keys."""
    pass

class RateLimitError(WalletError):
    """Raised when API requests exceed threshold."""
    def __init__(self, retry_after=60):
        super().__init__(f"Rate limit exceeded. Retry after {retry_after}s.")
        self.retry_after = retry_after