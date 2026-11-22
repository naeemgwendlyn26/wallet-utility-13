from typing import List, Dict, Optional

class WalletManager:
    """Handles core wallet operations and balance tracking."""

    def __init__(self, network: str) -> None:
        self.network: str = network
        self.balances: Dict[str, float] = {}

    def update_balance(self, address: str, amount: float) -> None:
        """Updates the stored balance for a specific wallet address."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.balances[address] = amount

    def get_total_value(self, addresses: List[str]) -> float:
        """Calculates cumulative balance for a list of addresses."""
        return sum(self.balances.get(addr, 0.0) for addr in addresses)

    def validate_address(self, address: str) -> bool:
        """Checks if a wallet address follows correct formatting."""
        return len(address) == 42 and address.startswith("0x")

    def get_active_wallets(self) -> List[str]:
        """Returns list of addresses with non-zero balances."""
        return [addr for addr, bal in self.balances.items() if bal > 0]

    def sync_network_state(self, remote_data: Dict[str, float]) -> None:
        """Synchronizes local state with external network nodes."""
        for address, balance in remote_data.items():
            if self.validate_address(address):
                self.update_balance(address, balance)