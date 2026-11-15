import json
import hashlib
from typing import Dict, Any


class CryptoPayloadHandler:
    """Utility class to validate, format, and hash crypto transaction payloads."""

    def __init__(self, chain_id: int = 1):
        self.chain_id = chain_id

    def sanitize_address(self, address: str) -> str:
        """Normalizes an Ethereum-style hex address to lower-case with 0x prefix."""
        cleaned = address.strip().lower()
        if not cleaned.startswith("0x"):
            cleaned = "0x" + cleaned
        if len(cleaned) != 42:
            raise ValueError(f"Invalid address length: {len(cleaned)}")
        return cleaned

    def parse_transaction(self, raw_tx: Dict[str, Any]) -> Dict[str, Any]:
        """Parses raw transaction dictionary and validates required fields."""
        required = ["to", "value", "nonce"]
        missing = [field for field in required if field not in raw_tx]
        if missing:
            raise KeyError(f"Missing transaction fields: {', '.join(missing)}")

        to_addr = self.sanitize_address(str(raw_tx["to"]))
        value = int(raw_tx["value"])
        nonce = int(raw_tx["nonce"])
        gas_limit = int(raw_tx.get("gas_limit", 21000))
        gas_price = int(raw_tx.get("gas_price", 20000000000))

        return {
            "chain_id": self.chain_id,
            "to": to_addr,
            "value": value,
            "nonce": nonce,
            "gas_limit": gas_limit,
            "gas_price": gas_price,
            "data": str(raw_tx.get("data", "0x")),
        }

    def compute_payload_hash(self, parsed_tx: Dict[str, Any]) -> str:
        """Generates SHA-256 hash of deterministic transaction payload JSON."""
        tx_bytes = json.dumps(parsed_tx, sort_keys=True).encode("utf-8")
        return hashlib.sha256(tx_bytes).hexdigest()
