import hashlib
import secrets
from typing import Optional

def generate_secure_entropy(length: int = 32) -> str:
    """Generates a cryptographically secure hex string."""
    return secrets.token_hex(length)

def mask_address(address: str, visible_chars: int = 6) -> str:
    """Masks a crypto address for UI display purposes."""
    if len(address) <= visible_chars * 2:
        return address
    return f"{address[:visible_chars]}...{address[-visible_chars:]}"

def validate_checksum(address: str) -> bool:
    """Basic validation for hex-based address formats."""
    if not address.startswith('0x') or len(address) != 42:
        return False
    return all(c in '0123456789abcdefABCDEF' for c in address[2:])

def derive_hash(data: str) -> str:
    """Derives a SHA-256 hash for data integrity checks."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def format_wei_to_eth(wei_value: int) -> float:
    """Converts raw wei integers to standard ether floats."""
    return wei_value / 10**18