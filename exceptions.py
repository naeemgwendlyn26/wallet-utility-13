"""Exception classes for wallet-utility-13 crypto operations.

This module centralizes all custom exceptions for better error handling
and reorganization of the codebase.
"""

class WalletError(Exception):
    """Base class for all wallet utility exceptions."""
    def __init__(self, message: str, error_code: int = 0):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"


class InvalidAddressError(WalletError):
    """Raised when a provided wallet address is invalid."""
    def __init__(self, address: str):
        message = f"Invalid wallet address format: {address}"
        super().__init__(message, 1001)
        self.address = address


class InsufficientBalanceError(WalletError):
    """Raised when attempting a transaction with insufficient funds."""
    def __init__(self, required: float, available: float, asset: str = "ETH"):
        message = f"Insufficient {asset} balance: required {required}, available {available}"
        super().__init__(message, 1002)
        self.required = required
        self.available = available
        self.asset = asset


class TransactionFailedError(WalletError):
    """Raised when a blockchain transaction fails to complete."""
    def __init__(self, tx_hash: str, reason: str):
        message = f"Transaction {tx_hash} failed: {reason}"
        super().__init__(message, 1003)
        self.tx_hash = tx_hash
        self.reason = reason


class NetworkConnectionError(WalletError):
    """Raised for issues connecting to blockchain networks."""
    def __init__(self, network: str, details: str):
        message = f"Network error on {network}: {details}"
        super().__init__(message, 1004)
        self.network = network
        self.details = details


class PrivateKeyError(WalletError):
    """Raised for problems with private key handling."""
    def __init__(self, message: str):
        super().__init__(message, 1005)


class SignatureVerificationError(WalletError):
    """Raised when signature verification fails."""
    def __init__(self, signature: str, expected: str):
        message = f"Signature verification failed for {signature}, expected {expected}"
        super().__init__(message, 1006)
        self.signature = signature


class UnsupportedOperationError(WalletError):
    """Raised for unsupported crypto operations or chains."""
    def __init__(self, operation: str, chain: str):
        message = f"Operation '{operation}' not supported on {chain}"
        super().__init__(message, 1007)
        self.operation = operation
        self.chain = chain