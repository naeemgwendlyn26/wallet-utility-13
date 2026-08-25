import json
from typing import Dict, List, Any

class WalletHandler:
    def __init__(self, address: str, initial_balance: float = 0.0) -> None:
        self.address = address
        self.balance = initial_balance
        self.transactions: List[Dict[str, Any]] = []

    def process_transaction(self, tx_data: Dict[str, Any]) -> bool:
        if not self._is_valid_tx(tx_data):
            return False
        if tx_data.get('from') == self.address:
            self.balance -= tx_data.get('amount', 0)
        elif tx_data.get('to') == self.address:
            self.balance += tx_data.get('amount', 0)
        self.transactions.append(tx_data)
        return True

    def _is_valid_tx(self, tx: Dict[str, Any]) -> bool:
        required = {'from', 'to', 'amount', 'timestamp'}
        if not required.issubset(tx.keys()):
            return False
        try:
            amount = float(tx['amount'])
            if amount <= 0:
                return False
        except (ValueError, TypeError):
            return False
        return True

    def get_transaction_history(self) -> List[Dict[str, Any]]:
        return list(self.transactions)

    def save_to_file(self, filepath: str) -> None:
        data = {
            'address': self.address,
            'balance': self.balance,
            'transactions': self.transactions
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filepath: str) -> bool:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            self.address = data['address']
            self.balance = data.get('balance', 0.0)
            self.transactions = data.get('transactions', [])
            return True
        except Exception:
            return False

    def get_balance(self) -> float:
        return self.balance

if __name__ == '__main__':
    wh = WalletHandler('0xabc123')
    tx = {'from': '0xabc123', 'to': '0xdef456', 'amount': 5.0, 'timestamp': 'now'}
    wh.process_transaction(tx)
    print(wh.get_balance())
    wh.save_to_file('wallet.json')