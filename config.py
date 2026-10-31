import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG_PATH = Path.home() / ".wallet_utility" / "config.json"

DEFAULT_SETTINGS: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.1,
    "enable_cache": True,
}


@dataclass
class WalletConfig:
    network: str = DEFAULT_SETTINGS["network"]
    rpc_url: str = DEFAULT_SETTINGS["rpc_url"]
    request_timeout: int = DEFAULT_SETTINGS["request_timeout"]
    max_retries: int = DEFAULT_SETTINGS["max_retries"]
    gas_limit_multiplier: float = DEFAULT_SETTINGS["gas_limit_multiplier"]
    enable_cache: bool = DEFAULT_SETTINGS["enable_cache"]

    @classmethod
    def load(cls, config_path: Optional[Path] = None) -> "WalletConfig":
        """Load configuration from a JSON file and environment variables."""
        path = config_path or DEFAULT_CONFIG_PATH
        config_data = DEFAULT_SETTINGS.copy()

        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    config_data.update(file_data)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config from {path}: {err}")

        # Override with environment variables if present
        env_network = os.getenv("WALLET_NETWORK")
        if env_network:
            config_data["network"] = env_network

        env_rpc = os.getenv("WALLET_RPC_URL")
        if env_rpc:
            config_data["rpc_url"] = env_rpc

        return cls(
            network=str(config_data.get("network", DEFAULT_SETTINGS["network"])),
            rpc_url=str(config_data.get("rpc_url", DEFAULT_SETTINGS["rpc_url"])),
            request_timeout=int(config_data.get("request_timeout", DEFAULT_SETTINGS["request_timeout"])),
            max_retries=int(config_data.get("max_retries", DEFAULT_SETTINGS["max_retries"])),
            gas_limit_multiplier=float(config_data.get("gas_limit_multiplier", DEFAULT_SETTINGS["gas_limit_multiplier"])),
            enable_cache=bool(config_data.get("enable_cache", DEFAULT_SETTINGS["enable_cache"])),
        )
