import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://eth.llamarpc.com",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load config file: {e}. Using defaults.")
            
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Helper to fetch specific configuration values."""
    config = load_config()
    return config.get(key, default)