import decimal
from typing import Union

def wei_to_ether(wei_value: Union[int, str]) -> float:
    """Convert wei (smallest unit) to ether."""
    return float(decimal.Decimal(str(wei_value)) / decimal.Decimal(10**18))

def ether_to_wei(ether_value: Union[float, str]) -> int:
    """Convert ether to wei for smart contract calls."""
    return int(decimal.Decimal(str(ether_value)) * decimal.Decimal(10**18))

def format_address(address: str) -> str:
    """Standardize address formatting for consistency."""
    if not address.startswith('0x'):
        address = f'0x{address}'
    return address.lower()

def validate_gas_price(gas_price_gwei: float) -> bool:
    """Check if gas price is within reasonable range."""
    return 0.1 <= gas_price_gwei <= 1000.0

def calculate_tx_fee(gas_limit: int, gas_price_gwei: float) -> float:
    """Calculate total transaction cost in ether."""
    fee_wei = gas_limit * (gas_price_gwei * 10**9)
    return wei_to_ether(int(fee_wei))