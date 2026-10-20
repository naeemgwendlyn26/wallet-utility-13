import os
from typing import Dict, Optional

class WalletManager:
    """Handles crypto wallet operations for wallet-utility-13."""

    def __init__(self, network: str = "mainnet"):
        self.network = network
        self._cache: Dict[str, str] = {}

    def get_wallet_address(self, public_key: str) -> Optional[str]:
        """Derives address from public key with caching."""
        if public_key in self._cache:
            return self._cache[public_key]

        if len(public_key) < 32:
            return None

        address = f"0x{public_key[:40].lower()}"
        self._cache[public_key] = address
        return address

    def validate_config(self) -> bool:
        """Check environment variables for wallet connectivity."""
        return "RPC_URL" in os.environ

    def reset_session(self) -> None:
        """Clear local cache for security and memory."""
        self._cache.clear()

if __name__ == "__main__":
    manager = WalletManager()
    print(f"Initialized wallet manager on {manager.network}")