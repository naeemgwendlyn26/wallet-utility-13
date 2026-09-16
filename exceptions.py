class WalletError(Exception):
    """Base exception for all wallet operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is below transaction cost."""
    def __init__(self, required, actual):
        super().__init__(f"Required {required}, but only {actual} available.")

class InvalidAddressError(WalletError):
    """Raised when a crypto address format is invalid."""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when connection to the node times out."""
    pass

class SigningError(WalletError):
    """Raised when transaction signature fails."""
    pass

class ConfigurationError(WalletError):
    """Raised when wallet settings are invalid."""
    pass

def raise_if_insufficient(balance: float, amount: float, fee: float):
    """Validation helper for balance checks."""
    if balance < (amount + fee):
        raise InsufficientFundsError(amount + fee, balance)