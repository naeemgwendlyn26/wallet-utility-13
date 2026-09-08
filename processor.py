import re
from typing import Dict, Any, Optional

def validate_transaction_fields(tx: Dict[str, Any]) -> bool:
    """
    Validates that the transaction dictionary contains all required fields
    with correct types and formats.
    """
    required_keys = {"to", "value", "gas_price", "gas", "nonce"}
    if not required_keys.issubset(tx.keys()):
        return False

    # Validate address format (simple hex check)
    if not isinstance(tx["to"], str) or not re.match(r"^0x[0-9a-fA-F]{40}$", tx["to"]):
        return False

    # Validate numeric fields
    numeric_fields = ["value", "gas_price", "gas", "nonce"]
    for field in numeric_fields:
        if not isinstance(tx[field], int) or tx[field] < 0:
            return False

    return True

def calculate_total_cost(tx: Dict[str, Any]) -> Optional[int]:
    """
    Calculates the maximum cost of the transaction in wei.
    Total Cost = Value + (Gas Limit * Gas Price)
    """
    if not validate_transaction_fields(tx):
        return None
    return tx["value"] + (tx["gas"] * tx["gas_price"])

def format_wei_to_gwei(wei: int) -> float:
    """
    Converts wei to gwei for easier readability.
    """
    return wei / 1_000_000_000

def format_gwei_to_wei(gwei: float) -> int:
    """
    Converts gwei to wei.
    """
    return int(gwei * 1_000_000_000)