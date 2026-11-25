class WalletError(Exception):
    """Base exception for wallet-utility-13."""
    pass

class ValidationError(WalletError):
    """Raised when input data fails schema validation."""
    pass

def validate_address(address: str) -> bool:
    """Basic length and hex validation for crypto addresses."""
    if not isinstance(address, str):
        raise ValidationError("Address must be a string.")
    if len(address) < 26 or len(address) > 35:
        raise ValidationError("Invalid address length.")
    if not address.isalnum():
        raise ValidationError("Address contains invalid characters.")
    return True

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and non-zero."""
    if not isinstance(amount, (int, float)):
        raise ValidationError("Amount must be numeric.")
    if amount <= 0:
        raise ValidationError("Amount must be greater than zero.")
    return True