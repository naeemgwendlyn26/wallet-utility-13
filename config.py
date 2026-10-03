import json
import os
from typing import Any, Dict

# Default configuration for wallet-utility-13
DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/your-api-key",
    "timeout_seconds": 30,
    "max_retries": 3,
    "gas_multiplier": 1.1,
    "enable_metrics": True,
}

class ConfigLoader:
    """Loads and manages configuration for the crypto wallet utility."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configuration from file and environment variables."""
        # Load from file if it exists
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
            except (json.JSONDecodeError, IOError):
                # Fallback to defaults if file is corrupted
                pass

        # Override with environment variables using WALLET_ prefix
        for key in self.config:
            env_key = f"WALLET_{key.upper()}"
            env_val = os.getenv(env_key)
            if env_val is not None:
                default_val = DEFAULT_CONFIG[key]
                if isinstance(default_val, bool):
                    self.config[key] = env_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    self.config[key] = int(env_val)
                elif isinstance(default_val, float):
                    self.config[key] = float(env_val)
                else:
                    self.config[key] = env_val

    def get(self, key: str) -> Any:
        """Retrieves a configuration value."""
        return self.config.get(key)