import hashlib
import hmac
from typing import Dict, Any
import json

def generate_signature(api_secret: str, payload: Dict[str, Any]) -> str:
    """Creates an HMAC-SHA256 signature for API authentication."""
    query_string = json.dumps(payload, sort_keys=True)
    return hmac.new(
        api_secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Standardizes crypto float representation to string format."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    
    format_str = f"{{:.{precision}f}}"
    return format_str.format(amount).rstrip('0').rstrip('.')

def validate_transaction_data(data: Dict[str, Any]) -> bool:
    """Ensures required fields exist in transaction payload."""
    required = {'asset', 'amount', 'address', 'nonce'}
    return all(key in data for key in required)

def sanitize_address(address: str) -> str:
    """Normalizes hex address strings to lowercase."""
    return address.strip().lower()