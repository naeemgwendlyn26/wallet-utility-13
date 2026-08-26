import hashlib
import base58

def validate_bitcoin_address(address: str) -> bool:
    """Validate a Bitcoin legacy address using base58 checksum."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 35:
        return False
    
    try:
        decoded = base58.b58decode(address)
        if len(decoded) != 25:
            return False
        
        payload = decoded[:-4]
        checksum = decoded[-4:]
        calculated_checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        
        return checksum == calculated_checksum
    except Exception:
        return False

def satoshis_to_btc(satoshis: int) -> float:
    """Convert satoshis to whole bitcoins."""
    if not isinstance(satoshis, int):
        raise TypeError("Satoshis must be an integer")
    return satoshis / 100000000.0

def btc_to_satoshis(btc: float) -> int:
    """Convert whole bitcoins to satoshis."""
    if not isinstance(btc, (int, float)):
        raise TypeError("BTC amount must be numeric")
    return int(round(btc * 100000000))

def mask_wallet_address(address: str) -> str:
    """Mask a wallet address for safe logging display."""
    if not isinstance(address, str) or len(address) < 10:
        return "***"
    return f"{address[:6]}...{address[-4:]}"
