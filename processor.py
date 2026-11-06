from typing import List, Dict, Optional

class TransactionProcessor:
    """Handles crypto transaction validation and serialization."""

    def __init__(self, network_fee: float = 0.001) -> None:
        self.network_fee: float = network_fee

    def calculate_total(self, amount: float) -> float:
        """Calculates total with network fee."""
        return amount + self.network_fee

    def format_batch(self, transactions: List[Dict[str, float]]) -> List[Dict[str, float]]:
        """Applies fees to a list of transactions."""
        processed: List[Dict[str, float]] = []
        for tx in transactions:
            tx['total'] = self.calculate_total(tx.get('amount', 0.0))
            processed.append(tx)
        return processed

    def validate_address(self, address: str) -> bool:
        """Checks format of crypto wallet address."""
        return len(address) == 42 and address.startswith('0x')

    def get_summary(self, tx_id: str, status: Optional[str] = None) -> Dict[str, str]:
        """Retrieves transaction status report."""
        return {
            "id": tx_id,
            "status": status or "pending"
        }