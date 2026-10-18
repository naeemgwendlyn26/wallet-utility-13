"""Custom exceptions for wallet-utility-13 crypto operations."""


class WalletError(Exception):
    """Base exception class for all crypto wallet utility errors."""

    def __init__(self, message: str, payload: dict = None):
        super().__init__(message)
        self.message = message
        self.payload = payload or {}


class InvalidAddressError(WalletError):
    """Raised when a crypto address fails checksum or format validation."""

    pass


class InsufficientBalanceError(WalletError):
    """Raised when an account lacks required funds for transfer or gas."""

    def __init__(self, required: float, available: float, currency: str = "ETH"):
        message = f"Insufficient balance: required {required} {currency}, available {available} {currency}"
        payload = {"required": required, "available": available, "currency": currency}
        super().__init__(message, payload)


class TransactionExecutionError(WalletError):
    """Raised when transaction broadcast or execution fails on-chain."""

    def __init__(self, tx_hash: str, reason: str):
        message = f"Transaction {tx_hash} failed: {reason}"
        super().__init__(message, payload={"tx_hash": tx_hash, "reason": reason})


class RPCNodeError(WalletError):
    """Raised when the connected RPC node returns an error or times out."""

    def __init__(self, endpoint: str, status_code: int, details: str):
        message = f"RPC node at {endpoint} returned error {status_code}: {details}"
        payload = {"endpoint": endpoint, "status_code": status_code, "details": details}
        super().__init__(message, payload)
