import hashlib
import hmac
from typing import Dict, Any, Optional

def generate_signature(api_secret: str, message: str) -> str:
    """Creates an HMAC SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_transaction(tx_data: Dict[str, Any]) -> Dict[str, Any]:
    """Cleans raw transaction dictionary for further processing."""
    required_keys = ['txid', 'amount', 'currency', 'timestamp']
    return {k: tx_data.get(k) for k in required_keys}

def format_balance(balance_data: Dict[str, Any]) -> str:
    """Converts raw balance unit to human readable string."""
    raw_val = balance_data.get('amount', 0)
    asset = balance_data.get('asset', 'UNKNOWN')
    try:
        return f"{float(raw_val):.8f} {asset}"
    except (ValueError, TypeError):
        return f"0.00000000 {asset}"

def validate_payload(data: Optional[Dict[str, Any]]) -> bool:
    """Checks if the transaction payload is complete."""
    if not data or not isinstance(data, dict):
        return False
    return all(key in data for key in ['txid', 'amount'])