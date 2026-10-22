import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "api_key": None
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from json file with fallback defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}. Using defaults.")
            
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Basic validation for essential configuration keys.
    """
    required = ["network"]
    return all(key in config for key in required)