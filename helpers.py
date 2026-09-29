from typing import Dict, Any, Optional
import decimal

def format_crypto_amount(amount: str, decimals: int = 18) -> decimal.Decimal:
    """Converts raw string amount from blockchain to human-readable decimal."""
    try:
        return decimal.Decimal(amount) / decimal.Decimal(10 ** decimals)
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0')

def sanitize_address(address: str) -> str:
    """Standardizes ethereum-like addresses to checksum lowercase format."""
    return address.strip().lower()

def get_gas_price_multiplier(priority: str = 'medium') -> float:
    """Calculates multiplier for transaction gas fees based on network congestion."""
    multipliers = {
        'low': 1.0,
        'medium': 1.2,
        'high': 1.5
    }
    return multipliers.get(priority.lower(), 1.2)

def validate_tx_payload(data: Dict[str, Any]) -> bool:
    """Ensures all required fields exist for wallet transaction submission."""
    required_fields = ['to', 'value', 'data']
    return all(field in data for field in required_fields)

def calculate_fee(gas_limit: int, gas_price_wei: int) -> int:
    """Determines transaction fee in wei given gas limits and prices."""
    return gas_limit * gas_price_wei