import re

# Crypto address validation patterns
ADDRESS_PATTERNS = {
    'BTC': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
    'ETH': r'^0x[a-fA-F0-9]{40}$'
}

def validate_wallet_address(address: str, chain: str) -> bool:
    """Validates address format based on blockchain type."""
    pattern = ADDRESS_PATTERNS.get(chain.upper())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Checks if the amount is a positive numeric string."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_payload(data: dict) -> bool:
    """Ensures dictionary contains valid transaction keys."""
    required = ['address', 'amount', 'chain']
    if not all(key in data for key in required):
        return False
    
    if not validate_wallet_address(data['address'], data['chain']):
        return False
        
    if not validate_amount(str(data['amount'])):
        return False
        
    return True