import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_price_multiplier": 1.2
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from json file with fallback to defaults
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config file {filepath}: {e}")
    
    return config

def get_wallet_env() -> str:
    """
    Get environment setting from system or config
    """
    return os.getenv("WALLET_ENV", "production")

if __name__ == "__main__":
    # Example usage for wallet-utility-13
    current_config = load_config()
    print(f"Loaded config: {current_config}")