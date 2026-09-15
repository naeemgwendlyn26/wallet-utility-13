from typing import Optional

class WalletError(Exception):
    """Base exception for all wallet-utility-13 operations."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class InsufficientFundsError(WalletError):
    """Raised when the balance is lower than the transaction amount."""
    pass

class ConnectionTimeoutError(WalletError):
    """Raised when the RPC node fails to respond in time."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a provided crypto address fails validation."""
    pass

class TransactionSigningError(WalletError):
    """Raised when a cryptographic signature fails generation."""
    pass

class DatabaseConnectionError(WalletError):
    """Raised when local state storage is inaccessible."""
    pass