import re
from typing import Any, Dict


class ValidationError(Exception):
    """Custom exception raised for invalid wallet or transaction inputs."""
    pass


def validate_ethereum_address(address: str) -> bool:
    """Check if the string is a valid hex-encoded Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def validate_amount(amount: Any) -> float:
    """Validate and convert transaction amount to a positive float."""
    try:
        parsed_amount = float(amount)
        if parsed_amount <= 0:
            raise ValidationError("Transaction amount must be greater than zero.")
        return parsed_amount
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid numeric amount format: '{amount}'")


def validate_input_batch(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a batch processing item for the main execution loop."""
    required_keys = ["recipient", "amount", "chain"]
    for key in required_keys:
        if key not in payload:
            raise ValidationError(f"Missing required field in payload: '{key}'")

    address = str(payload["recipient"])
    if not validate_ethereum_address(address):
        raise ValidationError(f"Invalid recipient address format: '{address}'")

    validated_amount = validate_amount(payload["amount"])

    chain = str(payload["chain"]).lower()
    allowed_chains = {"ethereum", "polygon", "arbitrum", "optimism"}
    if chain not in allowed_chains:
        supported = ", ".join(sorted(allowed_chains))
        raise ValidationError(f"Unsupported chain '{chain}'. Allowed: {supported}")

    return {
        "recipient": address,
        "amount": validated_amount,
        "chain": chain,
        "gas_limit": int(payload.get("gas_limit", 21000)),
    }
