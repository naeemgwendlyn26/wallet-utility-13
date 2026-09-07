import logging
from typing import Optional, Dict

# Configure logging for wallet-utility-13
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wallet_utility')

def format_address(address: str) -> str:
    """Truncate crypto address for display."""
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"

def validate_amount(amount: str) -> Optional[float]:
    """Ensure amount is a positive float."""
    try:
        value = float(amount)
        return value if value > 0 else None
    except (ValueError, TypeError):
        return None

def get_network_fee(gas_price: int, gas_limit: int) -> float:
    """Calculate fee in ETH based on gas parameters."""
    return (gas_price * gas_limit) / 10**18

def parse_transaction_data(data: Dict) -> Dict:
    """Sanitize transaction dictionary for processing."""
    return {
        "to": data.get("to", "").lower(),
        "value": float(data.get("value", 0)),
        "nonce": int(data.get("nonce", 0))
    }