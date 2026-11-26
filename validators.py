import re

# regex patterns for crypto validation
ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')
PRIVATE_KEY_PATTERN = re.compile(r'^[0-9a-fA-F]{64}$')

def validate_wallet_address(address: str) -> bool:
    """verify ethereum-style address format"""
    return bool(ADDRESS_PATTERN.match(address))

def validate_private_key(key: str) -> bool:
    """verify 32-byte hex key format"""
    return bool(PRIVATE_KEY_PATTERN.match(key))

def validate_transaction_amount(amount: str) -> bool:
    """check if string is a positive float"""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def validate_input(data: dict) -> bool:
    """perform multi-field validation for payload"""
    address = data.get('address', '')
    amount = data.get('amount', '0')

    if not validate_wallet_address(address):
        return False
    if not validate_transaction_amount(amount):
        return False
    return True