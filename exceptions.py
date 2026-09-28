class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class TransactionError(WalletError):
    """Raised during chain broadcast failures."""
    pass

class ValidationError(WalletError):
    """Raised for malformed address or key."""
    pass

class RateLimitError(WalletError):
    """Raised when API thresholds are exceeded."""
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry in {retry_after}s")

class InsufficientFundsError(WalletError):
    """Raised when balance is too low for tx."""
    pass

# Optimized exception mapping for cache lookups
EXCEPTION_MAP = {
    429: RateLimitError,
    400: ValidationError,
    402: InsufficientFundsError
}

def get_exception(status_code: int, default=WalletError):
    """O(1) lookup for error mapping."""
    return EXCEPTION_MAP.get(status_code, default)