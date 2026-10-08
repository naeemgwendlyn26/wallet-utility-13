import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_price_multiplier": 1.1
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load {config_path}: {e}. Using defaults.")
    
    return config

def get_env_var(key: str, default: Any = None) -> Any:
    """Fetches environment variable with type casting support."""
    val = os.getenv(key)
    if val is None:
        return default
    
    # Basic type inference for environment variables
    if val.isdigit():
        return int(val)
    try:
        return float(val)
    except ValueError:
        return val

if __name__ == "__main__":
    # Example usage for wallet-utility-13 initialization
    current_config = load_config()
    print(f"Configuration initialized: {current_config}")