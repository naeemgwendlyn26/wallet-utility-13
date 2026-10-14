import os
from typing import Dict, Any, Optional

class WalletConfig:
    """
    Configuration management for wallet-utility-13.
    Handles environment variables and network settings.
    """

    def __init__(self) -> None:
        self.rpc_url: str = os.getenv("RPC_URL", "https://mainnet.infura.io/v3/default")
        self.timeout: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    def get_network_settings(self) -> Dict[str, Any]:
        """
        Returns dictionary of network configuration parameters.

        Returns:
            Dict[str, Any]: Current network settings.
        """
        return {
            "url": self.rpc_url,
            "timeout": self.timeout,
            "debug_mode": self.debug
        }

    def update_timeout(self, new_timeout: int) -> None:
        """
        Updates the request timeout value dynamically.

        Args:
            new_timeout (int): New timeout duration in seconds.
        """
        if new_timeout > 0:
            self.timeout = new_timeout

def load_config() -> WalletConfig:
    """
    Factory function for WalletConfig instance.

    Returns:
        WalletConfig: Initialized configuration object.
    """
    return WalletConfig()