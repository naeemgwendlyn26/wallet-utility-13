import json
import logging
from decimal import Decimal, InvalidOperation

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for payload processing failures."""
    pass

def process_transaction_payload(raw_payload: str) -> dict:
    """Parses and validates a raw cryptocurrency transaction payload."""
    if not raw_payload or not isinstance(raw_payload, str):
        raise ValueError("Payload must be a non-empty string")

    try:
        data = json.loads(raw_payload)
    except json.JSONDecodeError as err:
        logger.error(f"Invalid JSON payload: {err}")
        raise ProcessingError("Malformed JSON payload provided") from err

    required_keys = {"sender", "recipient", "amount"}
    if not required_keys.issubset(data.keys()):
        missing = required_keys - set(data.keys())
        raise ProcessingError(f"Missing required payload fields: {', '.join(missing)}")

    try:
        amount = Decimal(str(data["amount"]))
        if amount <= 0:
            raise ProcessingError("Transaction amount must be strictly positive")
    except (InvalidOperation, TypeError) as err:
        raise ProcessingError("Invalid decimal amount specified") from err

    return {
        "sender": str(data["sender"]).strip(),
        "recipient": str(data["recipient"]).strip(),
        "amount": amount,
        "status": "validated"
    }
