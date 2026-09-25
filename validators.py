import re

def validate_address(address: str) -> bool:
    """Validate cryptocurrency address format."""
    # Basic hex regex for common EVM-compatible addresses
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Ensure input amount is a positive numeric string."""
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def process_input(data: dict) -> bool:
    """Main loop validation logic."""
    address = data.get("address", "")
    amount = data.get("amount", "")

    if not validate_address(address):
        return False
    
    if not validate_amount(str(amount)):
        return False
        
    return True