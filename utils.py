import hashlib
from typing import Optional

def generate_address_checksum(pubkey_hex: str) -> str:
    """Generates a standard EIP-55 style checksum for a hex address."""
    address = pubkey_hex.lower().replace('0x', '')
    hash_addr = hashlib.sha3_256(address.encode()).hexdigest()
    
    checksum_addr = '0x'
    for i in range(len(address)):
        if int(hash_addr[i], 16) >= 8:
            checksum_addr += address[i].upper()
        else:
            checksum_addr += address[i]
    return checksum_addr

def validate_transaction_fee(gas_price: int, gas_limit: int, balance: int) -> bool:
    """Verifies if wallet balance covers the estimated transaction cost."""
    required_fee = gas_price * gas_limit
    return balance >= required_fee

def format_wei_to_eth(wei_amount: int) -> float:
    """Converts raw wei integers to readable ether floats."""
    return float(wei_amount) / 1e18

def sanitize_hex(data: Optional[str]) -> str:
    """Ensures hex strings contain proper prefixes."""
    if not data:
        return '0x0'
    return data if data.startswith('0x') else f'0x{data}'