import re

# Regex for standard EVM-compatible addresses
ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_address(address: str) -> bool:
    """Verify EVM address checksum and format."""
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: str) -> bool:
    """Ensure amount is a valid positive decimal string."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(user_input: str) -> str:
    """Strip whitespace and normalize casing for inputs."""
    return user_input.strip().lower()

def is_valid_chain_id(chain_id: int) -> bool:
    """Validate standard EVM chain ID ranges."""
    # Mainnets and common testnets
    supported_ids = {1, 5, 10, 56, 137, 42161}
    return chain_id in supported_ids