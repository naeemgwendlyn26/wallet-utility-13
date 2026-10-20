import hashlib
import hmac
from typing import Optional

def generate_address_checksum(address: str) -> str:
    """Generates EIP-55 style checksum for address."""
    address = address.lower().replace('0x', '')
    hash_addr = hashlib.sha3_256(address.encode()).hexdigest()
    checksum = '0x'
    for i in range(len(address)):
        if int(hash_addr[i], 16) >= 8:
            checksum += address[i].upper()
        else:
            checksum += address[i]
    return checksum

def validate_fee_bounds(amount: float, min_val: float, max_val: float) -> bool:
    """Ensures fee is within acceptable network range."""
    return min_val <= amount <= max_val

def format_wei_to_eth(wei: int) -> float:
    """Converts raw wei integers to float ether."""
    return float(wei) / 10**18

def sign_payload(payload: str, secret: str) -> str:
    """Creates HMAC signature for API requests."""
    return hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()