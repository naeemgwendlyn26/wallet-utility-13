import re

class WalletValidator:
    """Handles validation for crypto wallet inputs."""

    # Basic regex for hex-based wallet addresses
    ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

    @staticmethod
    def is_valid_address(address: str) -> bool:
        """Checks if provided string is a valid EVM-compatible address."""
        if not isinstance(address, str):
            return False
        return bool(WalletValidator.ADDRESS_PATTERN.match(address))

    @staticmethod
    def is_valid_amount(amount: str) -> bool:
        """Validates positive numerical string for transactions."""
        try:
            value = float(amount)
            return value > 0
        except (ValueError, TypeError):
            return False

def validate_transaction_data(data: dict) -> tuple[bool, str]:
    """Performs bulk validation on transaction payload."""
    address = data.get("address")
    amount = data.get("amount")

    if not WalletValidator.is_valid_address(address):
        return False, f"Invalid wallet address format: {address}"
    
    if not WalletValidator.is_valid_amount(amount):
        return False, f"Invalid transaction amount: {amount}"

    return True, "Validation successful"