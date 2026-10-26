import re

def validate_address(address: str) -> bool:
    """Verify ethereum-style address format."""
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    """Ensure transaction amount is positive."""
    return isinstance(amount, (int, float)) and amount > 0

def validate_payload(data: dict) -> bool:
    """Main loop input validation check."""
    required = ['address', 'amount', 'currency']
    if not all(k in data for k in required):
        return False
    if not validate_address(data['address']):
        return False
    if not validate_amount(data['amount']):
        return False
    return True