"""Custom exception hierarchy for crypto wallet operations."""


class WalletError(Exception):
    """Base exception class for wallet-utility operations."""

    def __init__(self, message: str, code: str = "WALLET_ERROR"):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"


class InvalidAddressError(WalletError):
    """Raised when a cryptocurrency address format or checksum is invalid."""

    def __init__(self, address: str, network: str = "unknown"):
        self.address = address
        self.network = network
        msg = f"Invalid address '{address}' for network '{network}'"
        super().__init__(msg, code="INVALID_ADDRESS")


class InsufficientFundsError(WalletError):
    """Raised when balance is insufficient for a transaction and gas fees."""

    def __init__(self, required: float, available: float, currency: str = "ETH"):
        self.required = required
        self.available = available
        self.currency = currency
        msg = f"Insufficient {currency}: required {required}, available {available}"
        super().__init__(msg, code="INSUFFICIENT_FUNDS")


class TransactionSigningError(WalletError):
    """Raised when cryptographic signature generation fails."""

    def __init__(self, tx_hash: str, reason: str):
        self.tx_hash = tx_hash
        self.reason = reason
        msg = f"Failed to sign transaction {tx_hash}: {reason}"
        super().__init__(msg, code="SIGNING_FAILED")


class CryptoNodeRPCError(WalletError):
    """Raised when node communication or JSON-RPC request fails."""

    def __init__(self, rpc_code: int, rpc_message: str):
        self.rpc_code = rpc_code
        self.rpc_message = rpc_message
        msg = f"RPC Node Error ({rpc_code}): {rpc_message}"
        super().__init__(msg, code="NODE_RPC_ERROR")
