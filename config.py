import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "provider_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "gas_limit": 21000,
    "timeout": 30,
    "enable_metrics": False
}

class ConfigLoader:
    """Loads and merges configuration for the crypto wallet utility."""

    def __init__(self, config_path: str = None):
        self.config_path = config_path
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        # Load from file if provided and exists
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
            except (json.JSONDecodeError, OSError):
                # Fallback silently on read/parse failures
                pass

        # Override with environment variables if present
        for key in self.config.keys():
            env_key = f"WALLET_{key.upper()}"
            env_val = os.getenv(env_key)
            if env_val is not None:
                current_val = self.config[key]
                if isinstance(current_val, bool):
                    self.config[key] = env_val.lower() in ("true", "1", "yes")
                elif isinstance(current_val, int):
                    try:
                        self.config[key] = int(env_val)
                    except ValueError:
                        pass
                else:
                    self.config[key] = env_val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self.config.get(key, default)
