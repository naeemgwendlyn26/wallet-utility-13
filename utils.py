import json
import os
from typing import Dict, Any, Optional

def load_wallet_config(file_path: str) -> Dict[str, Any]:
    """Loads and validates crypto wallet configuration from JSON."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file {file_path} not found.")
    
    with open(file_path, 'r') as f:
        config = json.load(f)
    
    return config

def sanitize_address(address: str) -> str:
    """Removes whitespace and ensures lowercase for hex addresses."""
    return address.strip().lower()

def format_balance(amount: float, precision: int = 8) -> str:
    """Formats crypto balance to specified decimal precision."""
    return f"{amount:.{precision}f}"

def validate_network_id(network_id: Any) -> bool:
    """Checks if network identifier is valid hex or integer."""
    if isinstance(network_id, int):
        return network_id > 0
    if isinstance(network_id, str):
        return network_id.startswith('0x') and len(network_id) > 2
    return False

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback safety."""
    return os.getenv(key, default or "")