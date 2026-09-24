import hashlib
import base58

def generate_address_checksum(pubkey_bytes: bytes) -> str:
    """Generates a base58 address for a given public key."""
    sha256_hash = hashlib.sha256(pubkey_bytes).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    return base58.b58encode_check(ripemd160_hash).decode('utf-8')

def validate_transaction_signature(signature: bytes, message: bytes, public_key: bytes) -> bool:
    """Verifies ECDSA signature integrity."""
    from ecdsa import VerifyingKey, SECP256k1
    try:
        vk = VerifyingKey.from_string(public_key, curve=SECP256k1)
        return vk.verify(signature, message)
    except Exception:
        return False

def format_satoshi_to_btc(satoshi_amount: int) -> float:
    """Converts satoshi integer to decimal btc."""
    return float(satoshi_amount) / 100_000_000

def calculate_fee(bytes_size: int, sat_per_byte: int) -> int:
    """Calculates total transaction fee in satoshis."""
    return bytes_size * sat_per_byte