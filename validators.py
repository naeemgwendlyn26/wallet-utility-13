import re

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    """Validate cryptocurrency wallet addresses for format compliance."""
    if not isinstance(address, str) or not address:
        return False

    if chain_type == 'evm':
        # Standard Ethereum address regex: 0x followed by 40 hex chars
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    
    if chain_type == 'btc':
        # Basic P2PKH/P2SH validation regex
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))

    return False

def validate_amount(amount: str) -> bool:
    """Ensure amount is a positive numeric string."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False
