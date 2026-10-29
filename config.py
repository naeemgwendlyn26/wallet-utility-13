import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.1,
    "enable_logging": True,
}


class ConfigLoader:
    """Manages loading and merging application settings for wallet operations."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file and env vars, merging with defaults."""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config file: {err}")

        env_network = os.getenv("WALLET_NETWORK")
        if env_network:
            self._config["network"] = env_network

        env_rpc = os.getenv("WALLET_RPC_URL")
        if env_rpc:
            self._config["rpc_url"] = env_rpc

        env_timeout = os.getenv("WALLET_TIMEOUT")
        if env_timeout and env_timeout.isdigit():
            self._config["request_timeout"] = int(env_timeout)

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a specific configuration parameter."""
        return self._config.get(key, default)
