class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class ValidationError(WalletError):
    """Exception raised for invalid input data."""
    pass

def validate_address(address: str) -> bool:
    """Validates cryptocurrency address format."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 35:
        raise ValidationError(f"Invalid address format: {address}")
    return True

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and non-zero."""
    if amount <= 0:
        raise ValidationError(f"Invalid amount: {amount}. Must be greater than zero.")
    return True

def validate_payload(data: dict):
    """Main validation gate for incoming requests."""
    required = ['address', 'amount', 'currency']
    for field in required:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
    
    validate_address(data['address'])
    validate_amount(data['amount'])
    return True