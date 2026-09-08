import hashlib
import hmac
from typing import Dict, Any
import json

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for API authentication."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_amount(amount: float, decimals: int = 8) -> str:
    """Formats float balances for strict crypto precision."""
    return f"{amount:.{decimals}f}"

def parse_response(response_text: str) -> Dict[str, Any]:
    """Safely parses JSON network responses."""
    try:
        return json.loads(response_text)
    except (json.JSONDecodeError, TypeError):
        return {}

def validate_address(address: str, prefix: str = '0x') -> bool:
    """Validates basic hex address structure."""
    if not address.startswith(prefix):
        return False
    return all(c in '0123456789abcdefABCDEF' for c in address[len(prefix):])

def calculate_fee(amount: float, fee_rate: float) -> float:
    """Calculates network transaction fee."""
    return round(amount * fee_rate, 8)