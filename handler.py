import decimal
from typing import Dict, Optional

def format_crypto_amount(amount: str, precision: int = 8) -> str:
    """Converts raw string amount to standardized decimal format."""
    try:
        value = decimal.Decimal(amount)
        return format(value.normalize(), f'f').rstrip('0').rstrip('.')
    except (decimal.InvalidOperation, ValueError):
        return "0"

def calculate_transaction_fee(amount: str, rate: float) -> str:
    """Calculates fee based on amount and multiplier."""
    val = decimal.Decimal(amount)
    fee = val * decimal.Decimal(str(rate))
    return str(fee.quantize(decimal.Decimal('0.00000001')))

def validate_address_format(address: str, chain: str) -> bool:
    """Validates address format based on network chain."""
    rules = {
        "ETH": lambda a: a.startswith("0x") and len(a) == 42,
        "BTC": lambda a: len(a) in [26, 34, 42, 62]
    }
    validator = rules.get(chain)
    return validator(address) if validator else False

def parse_wallet_data(data: Dict) -> Optional[Dict]:
    """Standardizes incoming wallet dictionary payloads."""
    if not data or 'balance' not in data:
        return None
    return {
        "address": data.get("address"),
        "balance": format_crypto_amount(data.get("balance", "0")),
        "timestamp": data.get("ts")
    }