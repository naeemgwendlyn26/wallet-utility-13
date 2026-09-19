import hashlib
import hmac
from decimal import Decimal
from typing import Union

def format_amount(amount: Union[str, float, int], precision: int = 8) -> Decimal:
    """Converts raw crypto amounts to standard decimal precision."""
    return Decimal(str(amount)).quantize(Decimal(f"1.{'0' * precision}"))

def generate_signature(api_secret: str, message: str) -> str:
    """Creates HMAC-SHA256 signature for API authentication."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def is_valid_address(address: str, prefix: str = '0x') -> bool:
    """Simple validation for standard hex-based crypto addresses."""
    if not address.startswith(prefix):
        return False
    return len(address) == 42 and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def wei_to_ether(wei: int) -> Decimal:
    """Converts smallest unit to base currency unit."""
    return Decimal(wei) / Decimal(10**18)