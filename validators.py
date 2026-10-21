import re

class AddressValidationError(Exception):
    """Custom exception for crypto address validation issues."""
    pass

def validate_evm_address(address: str) -> bool:
    """
    Validates EVM-compatible wallet addresses using regex.
    Raises AddressValidationError if input format is invalid.
    """
    if not isinstance(address, str):
        raise AddressValidationError("Address must be a string")
    
    # Check for hex prefix and standard length
    if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        raise AddressValidationError(f"Invalid format for address: {address}")
        
    return True

def sanitize_input(data: str) -> str:
    """
    Basic sanitization to prevent malformed string processing.
    """
    if not data:
        return ""
    return str(data).strip().lower()

def safe_check(address: str) -> bool:
    """
    Wrapper for validation with error containment.
    """
    try:
        return validate_evm_address(sanitize_input(address))
    except AddressValidationError:
        return False