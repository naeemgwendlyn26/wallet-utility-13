class WalletError(Exception):
    """Base exception for wallet-utility-13 errors."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when transaction amount exceeds available balance."""
    def __init__(self, required, available):
        self.message = f"Required {required} but only {available} available."
        super().__init__(self.message)

class InvalidAddressError(WalletError):
    """Raised when the provided address fails validation."""
    def __init__(self, address):
        self.message = f"Invalid crypto address format: {address}"
        super().__init__(self.message)

class NetworkTimeoutError(WalletError):
    """Raised when RPC or node requests time out."""
    def __init__(self, node_url):
        self.message = f"Connection to node {node_url} timed out."
        super().__init__(self.message)

class SignatureError(WalletError):
    """Raised during cryptographic signing failures."""
    pass

class DecryptionError(WalletError):
    """Raised when private keys cannot be decrypted."""
    pass