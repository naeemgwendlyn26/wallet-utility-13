import hashlib
import hmac
from decimal import Decimal
from typing import Union

def format_crypto_amount(amount: Union[str, float, Decimal], precision: int = 8) -> str:
    """Converts amount to a standardized decimal string format."""
    d = Decimal(str(amount))
    return format(d, f'.{precision}f').rstrip('0').rstrip('.')

def generate_signature(api_secret: str, payload: str) -> str:
    """Creates HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def validate_address_format(address: str, chain: str = 'eth') -> bool:
    """Simple heuristic validation for blockchain addresses."""
    if chain.lower() == 'eth':
        return len(address) == 42 and address.startswith('0x')
    elif chain.lower() == 'btc':
        return len(address) >= 26 and len(address) <= 35
    return False

def calculate_fee(amount: float, rate: float) -> Decimal:
    """Calculates network transaction fee based on rate."""
    return Decimal(str(amount)) * Decimal(str(rate))
