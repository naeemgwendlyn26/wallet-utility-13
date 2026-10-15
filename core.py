import hashlib
import hmac
from decimal import Decimal

def format_crypto_amount(amount: str, precision: int = 8) -> str:
    """Formats a string amount to fixed precision for display."""
    return f"{Decimal(amount):.{precision}f}"

def generate_hmac_signature(secret: str, message: str) -> str:
    """Generates a hex signature for API request authentication."""
    return hmac.new(
        secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def validate_address_format(address: str, prefix: str = '0x') -> bool:
    """Validates basic hex address string format."""
    if not address.startswith(prefix):
        return False
    return len(address) == 42 and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def convert_satoshi_to_btc(sats: int) -> float:
    """Converts satoshis to BTC float representation."""
    return float(Decimal(sats) / Decimal(10**8))