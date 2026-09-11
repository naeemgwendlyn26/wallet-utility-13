import re

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    """Validate cryptocurrency address formats."""
    if not isinstance(address, str) or not address:
        return False

    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain_type == 'btc':
        return bool(re.match(r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$', address))
    return False

def validate_amount(amount: str) -> bool:
    """Validate numeric string input for transactions."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(data: str) -> str:
    """Remove whitespace and strip potential control chars."""
    return ''.join(char for char in data.strip() if char.isprintable())