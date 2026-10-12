import re

def validate_address(address: str) -> bool:
    """Validate crypto address format using regex."""
    # Supports basic hex format for ETH/EVM compatible chains
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Ensure the provided string is a valid positive decimal."""
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def validate_transaction_input(address: str, amount: str) -> dict:
    """Consolidated validation for the main processing loop."""
    errors = []
    if not validate_address(address):
        errors.append("invalid wallet address format")
    if not validate_amount(amount):
        errors.append("invalid transaction amount")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

def sanitize_input(user_input: str) -> str:
    """Strip whitespace and potential control characters."""
    return user_input.strip().replace('\\', '')