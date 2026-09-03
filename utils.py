import hashlib
import os
from typing import Optional

def generate_checksum(data: bytes) -> str:
    """Generates SHA-256 hash for transaction data validation."""
    return hashlib.sha256(data).hexdigest()

def secure_random_hex(length: int = 32) -> str:
    """Generates cryptographically secure random hexadecimal string."""
    return os.urandom(length).hex()

def validate_address_format(address: str, prefix: str = '0x') -> bool:
    """Basic validation for crypto wallet address formatting."""
    if not address.startswith(prefix):
        return False
    return len(address) == 42 and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def format_wei_to_eth(wei: int) -> float:
    """Conversion from smallest unit to standard ether representation."""
    return wei / 10**18

class WalletUtility:
    def __init__(self, network: str = 'mainnet'):
        self.network = network

    def get_network_config(self) -> dict:
        """Retrieve base configuration based on selected network."""
        return {
            'mainnet': {'chain_id': 1, 'symbol': 'ETH'},
            'testnet': {'chain_id': 11155111, 'symbol': 'SEP'}
        }.get(self.network, {})
