import json
from typing import Dict, Any, Optional

def parse_crypto_payload(raw_data: str) -> Optional[Dict[str, Any]]:
    """
    Parses incoming raw JSON payload from crypto exchange WebSockets.
    Validates basic structure and extracts transaction details.
    """
    try:
        parsed = json.loads(raw_data)
        
        # Ensure the payload contains essential crypto transaction fields
        if not isinstance(parsed, dict):
            return None
            
        required_fields = {"txid", "amount", "currency", "wallet_address"}
        if not required_fields.issubset(parsed.keys()):
            return None
            
        # Normalize data types
        transaction = {
            "txid": str(parsed["txid"].strip()),
            "amount": float(parsed["amount"]),
            "currency": str(parsed["currency"].upper()),
            "wallet_address": str(parsed["wallet_address"].strip())
        }
        
        # Basic sanity check for amounts
        if transaction["amount"] <= 0:
            return None
            
        return transaction
        
    except (json.JSONDecodeError, ValueError, TypeError):
        # Return None on any parsing or casting failure
        return None

def format_wallet_response(status: str, data: Dict[str, Any]) -> str:
    """
    Formats outgoing response payload for wallet utility operations.
    """
    response_envelope = {
        "status": status,
        "payload": data,
        "utility": "wallet-utility-13"
    }
    return json.dumps(response_envelope)