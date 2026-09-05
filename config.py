import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "NETWORK": "mainnet",
    "RPC_URL": "https://rpc.ankr.com/eth",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "KEY_STORE_PATH": "./data/keys"
}

def load_config(overrides: Dict[str, Any] = None) -> Dict[str, Any]:
    """Merges default configuration with environment variables and provided overrides."""
    config = DEFAULT_CONFIG.copy()

    # Check environment for overrides
    for key in config:
        env_val = os.getenv(f"WALLET_{key}")
        if env_val:
            # Type casting based on default types
            target_type = type(config[key])
            config[key] = target_type(env_val)

    # Apply manual overrides if provided
    if overrides:
        config.update(overrides)

    return config

if __name__ == "__main__":
    # Example usage for wallet-utility-13
    current_cfg = load_config({"NETWORK": "sepolia"})
    print(f"Loaded config for {current_cfg.get('NETWORK')} network")