import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://rpc.ankr.com/eth",
    "request_timeout": 15,
    "max_retries": 3,
    "gas_price_multiplier": 1.15,
    "enable_cache": True,
    "cache_ttl_seconds": 300,
}

ENV_PREFIX = "WALLET_"


class ConfigLoader:
    """Loads and manages wallet utility configurations with sensible defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if config_path:
            self._load_from_file(config_path)
        self._load_from_env()

    def _load_from_file(self, path_str: str) -> None:
        path = Path(path_str).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            file_data = json.load(f)
            if isinstance(file_data, dict):
                self._config.update(file_data)

    def _load_from_env(self) -> None:
        for key, default_val in DEFAULT_CONFIG.items():
            env_var = f"{ENV_PREFIX}{key.upper()}"
            if env_var in os.environ:
                raw_val = os.environ[env_var]
                val_type = type(default_val)
                if val_type is bool:
                    self._config[key] = raw_val.lower() in ("true", "1", "yes")
                elif val_type in (int, float):
                    self._config[key] = val_type(raw_val)
                else:
                    self._config[key] = raw_val

    def get(self, key: str, fallback: Any = None) -> Any:
        return self._config.get(key, fallback)

    def as_dict(self) -> Dict[str, Any]:
        return self._config.copy()
