import json
from typing import Dict, Any, Optional

def format_transaction_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalizes raw crypto transaction data into a standardized dictionary format.
    Ensures fields are cast to appropriate types for wallet accounting.
    """
    try:
        return {
            "tx_hash": str(raw_data.get("hash", "")), 
            "amount": float(raw_data.get("value", 0)) / 1e18,  # Convert Wei to ETH
            "sender": str(raw_data.get("from", "")).lower(),
            "recipient": str(raw_data.get("to", "")).lower(),
            "gas_used": int(raw_data.get("gas", 0)),
            "is_confirmed": bool(raw_data.get("status", False))
        }
    except (ValueError, TypeError) as e:
        return {"error": "data parsing failure", "details": str(e)}

def calculate_net_balance(transactions: list) -> float:
    """
    Computes cumulative balance change from a list of transaction objects.
    """
    balance = 0.0
    for tx in transactions:
        # Simple logic: assume incoming is positive, outgoing is negative
        amount = tx.get("amount", 0)
        if tx.get("direction") == "inbound":
            balance += amount
        else:
            balance -= amount
    return balance