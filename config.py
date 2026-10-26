import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not parse {path}, using defaults")
            
    return config

def get_env_var(key: str, default: Any) -> Any:
    """Fetch environment variable with type-casted default."""
    val = os.getenv(key)
    if val is None:
        return default
    
    # Cast based on default type
    try:
        return type(default)(val)
    except (ValueError, TypeError):
        return default