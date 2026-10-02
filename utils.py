import hashlib
import json
from typing import Dict, Any, Optional

def sanitize_address(address: str) -> str:
    """Normalize cryptocurrency address strings for storage."""
    return address.strip().lower()

def generate_checksum(data: Dict[str, Any]) -> str:
    """Generate a SHA-256 hash for transaction validation."""
    serialized = json.dumps(data, sort_keys=True)
    return hashlib.sha256(serialized.encode('utf-8')).hexdigest()

def format_amount(amount: float, decimals: int = 8) -> float:
    """Round crypto values to specified precision."""
    return round(amount, decimals)

def validate_transaction_payload(payload: Dict[str, Any]) -> bool:
    """Ensure required fields exist in transaction data."""
    required_fields = {'from', 'to', 'amount', 'currency'}
    return all(field in payload for field in required_fields)

def parse_fee_data(fee_str: str) -> Optional[float]:
    """Convert fee string representation to float."""
    try:
        return float(fee_str.replace(' Gwei', '').strip())
    except (ValueError, AttributeError):
        return None