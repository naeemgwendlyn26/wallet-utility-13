import re

def validate_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    # Pattern for standard hex-based wallet addresses
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Ensure amount is a positive numerical value."""
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def process_transaction(address: str, amount: str):
    """Main loop entry point with input validation."""
    if not validate_address(address):
        raise ValueError(f"Invalid wallet address format: {address}")
    
    if not validate_amount(amount):
        raise ValueError(f"Invalid transaction amount: {amount}")
    
    # Proceed with transaction logic after validation
    print(f"Processing transfer of {amount} to {address}")
    return True