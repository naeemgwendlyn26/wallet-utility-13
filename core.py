import hashlib
from typing import Optional, Dict, Any

class WalletCore:
    """Handles cryptographic address generation and validation logic."""

    def __init__(self, network: str = "mainnet") -> None:
        self.network: str = network

    def generate_address_checksum(self, public_key: str) -> str:
        """Creates a SHA256 checksum for the provided public key."""
        sha_hash = hashlib.sha256(public_key.encode('utf-8')).hexdigest()
        return sha_hash[:8]

    def validate_transaction(self, tx_data: Dict[str, Any]) -> bool:
        """Checks if required fields exist in the transaction payload."""
        required_fields = {"sender", "receiver", "amount"}
        return required_fields.issubset(tx_data.keys())

    def format_balance(self, amount: float) -> str:
        """Converts float balance to a fixed precision string."""
        return f"{amount:.8f}"

    def get_network_info(self) -> Dict[str, str]:
        """Retrieves current environment configuration settings."""
        return {"network": self.network, "status": "active"}