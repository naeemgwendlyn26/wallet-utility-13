import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "derivation_path": "m/44'/60'/0'/0/0",
    "rpc_url": "https://cloudflare-eth.com",
    "request_timeout": 10,
    "max_retries": 3,
    "enable_logging": True
}

class ConfigLoader:
    """Loads configuration from environment variables, files, and defaults."""
    def __init__(self, filepath: str = None):
        self.config = DEFAULT_CONFIG.copy()
        if filepath:
            self.load_from_file(filepath)
        self.load_from_env()

    def load_from_file(self, filepath: str) -> None:
        """Loads configuration from a JSON file, overriding defaults."""
        if not os.path.exists(filepath):
            return
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                if isinstance(file_config, dict):
                    for key, val in file_config.items():
                        self.config[key.lower()] = val
        except (json.JSONDecodeError, OSError):
            # Silently fall back to defaults if parsing fails
            pass

    def load_from_env(self) -> None:
        """Loads configuration from environment variables with wallet prefix."""
        for key in DEFAULT_CONFIG:
            env_key = f"WALLET_{key.upper()}"
            env_val = os.getenv(env_key)
            if env_val is not None:
                default_val = DEFAULT_CONFIG[key]
                if isinstance(default_val, bool):
                    self.config[key] = env_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    try:
                        self.config[key] = int(env_val)
                    except ValueError:
                        pass
                else:
                    self.config[key] = env_val

    def get(self, key: str) -> Any:
        """Retrieves a config value by key name."""
        return self.config.get(key.lower())