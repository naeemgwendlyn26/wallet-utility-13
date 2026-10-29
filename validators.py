import re


def is_valid_eth_address(address: str) -> bool:
    """Check if the provided string is a valid Ethereum address format."""
    if not isinstance(address, str):
        return False
    # Check 0x prefix followed by 40 hexadecimal characters
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))


def is_valid_btc_address(address: str) -> bool:
    """Check if the string matches standard Bitcoin address formats."""
    if not isinstance(address, str):
        return False

    # Legacy (1...), P2SH (3...), Native SegWit (bc1...)
    legacy_p2sh = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    bech32 = r"^bc1[a-02-9ac-hj-np-z]{8,87}$"

    return bool(re.match(legacy_p2sh, address) or re.match(bech32, address))


def is_valid_solana_address(address: str) -> bool:
    """Check if the string is a valid Base58 Solana address format."""
    if not isinstance(address, str):
        return False
    # Solana public keys are 32-44 base58 characters
    pattern = r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"
    return bool(re.match(pattern, address))


def is_valid_hex_private_key(key: str) -> bool:
    """Validate 64-character raw hex private key format."""
    if not isinstance(key, str):
        return False
    clean_key = key.lower().removeprefix("0x")
    return bool(re.match(r"^[a-f0-9]{64}$", clean_key))
