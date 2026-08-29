"""Exception definitions for error handling in crypto wallet utility.
Provides custom exceptions for edge cases like invalid keys, addresses,
insufficient balances and network issues in crypto operations.
"""

class WalletError(Exception):
    """Base class for all wallet utility exceptions."""
    def __init__(self, message: str, error_code: int = 0) -> None:
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"[Code {self.error_code}] {self.message}"

class InvalidPrivateKeyError(WalletError):
    """Raised when private key does not meet crypto standards."""
    def __init__(self) -> None:
        super().__init__("Invalid or malformed private key", 1001)

class InvalidAddressError(WalletError):
    """Raised for wallet addresses that fail validation checks."""
    def __init__(self, address: str) -> None:
        super().__init__(f"Invalid wallet address: {address}", 1002)
        self.address = address

class InsufficientBalanceError(WalletError):
    """Raised when account balance is below required amount."""
    def __init__(self, balance: float, required: float) -> None:
        super().__init__(
            f"Insufficient balance: have {balance}, need {required}", 1003
        )
        self.balance = balance
        self.required = required

class InvalidAmountError(WalletError):
    """Raised for amounts that are zero or negative."""
    def __init__(self, amount: float) -> None:
        super().__init__(f"Amount must be positive, got {amount}", 1004)
        self.amount = amount

class NetworkError(WalletError):
    """Raised for connection or timeout issues with blockchain."""
    def __init__(self, message: str) -> None:
        super().__init__(f"Network error: {message}", 1005)

class UnsupportedTokenError(WalletError):
    """Raised when token symbol is not in supported list."""
    def __init__(self, token: str) -> None:
        super().__init__(f"Token {token} is not supported", 1006)
        self.token = token

class SignatureError(WalletError):
    """Raised on failure to sign or verify transaction."""
    def __init__(self, reason: str) -> None:
        super().__init__(f"Signature error: {reason}", 1007)

def handle_wallet_error(exc: Exception) -> dict:
    """Convert exception to standardized error dict for responses."""
    if isinstance(exc, WalletError):
        return {
            "success": False,
            "error_code": exc.error_code,
            "error_message": str(exc),
            "error_type": type(exc).__name__
        }
    return {
        "success": False,
        "error_code": 999,
        "error_message": "An unexpected error occurred",
        "error_type": "GenericError"
    }