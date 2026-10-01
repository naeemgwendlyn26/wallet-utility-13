import re
from typing import Any, Dict, Tuple


def validate_wallet_address(address: str) -> bool:
    """Validate Ethereum or Bitcoin style wallet addresses."""
    if not isinstance(address, str):
        return False
    eth_pattern = r"^0x[a-fA-F0-9]{40}$"
    btc_pattern = r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$"
    return bool(re.match(eth_pattern, address) or re.match(btc_pattern, address))


def validate_transaction_payload(payload: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate input payload structure and data types for crypto operations."""
    if not isinstance(payload, dict):
        return False, "Payload must be a valid dictionary"

    required_keys = {"recipient", "amount", "asset"}
    missing = required_keys - payload.keys()
    if missing:
        return False, f"Missing required payload fields: {', '.join(missing)}"

    address = payload.get("recipient")
    if not validate_wallet_address(str(address)):
        return False, f"Invalid destination wallet address: {address}"

    try:
        amount = float(payload.get("amount", 0))
        if amount <= 0:
            return False, "Transaction amount must be greater than zero"
    except (ValueError, TypeError):
        return False, "Transaction amount must be a valid numeric value"

    asset = payload.get("asset")
    if not isinstance(asset, str) or len(asset.strip()) == 0:
        return False, "Asset symbol must be a non-empty string"

    return True, "Payload validation successful"


def process_batch_inputs(batch: list) -> list:
    """Filter and return validated transactions from an input loop stream."""
    valid_records = []
    for item in batch:
        is_valid, _ = validate_transaction_payload(item)
        if is_valid:
            valid_records.append(item)
    return valid_records
