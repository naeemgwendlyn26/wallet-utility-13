class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when wallet balance is insufficient for transaction."""
    def __init__(self, requested: float, available: float):
        self.message = f"Insufficient funds: requested {requested}, available {available}"
        super().__init__(self.message)

class ConnectionTimeoutError(WalletError):
    """Raised when node connection fails."""
    pass

class InvalidAddressError(WalletError):
    """Raised when address format is invalid."""
    def __init__(self, address: str):
        self.message = f"Invalid crypto address format: {address}"
        super().__init__(self.message)

class SignatureError(WalletError):
    """Raised when transaction signing fails."""
    pass

class RateLimitError(WalletError):
    """Raised when API rate limits are exceeded."""
    def __init__(self, retry_after: int):
        self.message = f"Rate limit exceeded. Retry in {retry_after} seconds"
        super().__init__(self.message)