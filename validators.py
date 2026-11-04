import re

# regex patterns for crypto validation
ADDRESS_PATTERN = re.compile(r'^(0x[a-fA-F0-9]{40}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})$')

def validate_wallet_address(address: str) -> bool:
    """verify crypto address against standard hex or base58 patterns"""
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    """ensure transfer amount is positive and within logical bounds"""
    return isinstance(amount, (int, float)) and 0 < amount < 1000000

def process_input(data: dict) -> bool:
    """main entry point for transaction data validation"""
    try:
        address = data.get('address', '')
        amount = data.get('amount', 0)
        
        if not validate_wallet_address(address):
            return False
        if not validate_amount(amount):
            return False
            
        return True
    except (TypeError, ValueError):
        return False