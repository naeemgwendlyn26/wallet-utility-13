import json
import hashlib
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Transaction:
    tx_id: str
    from_address: str
    to_address: str
    amount: float
    timestamp: int

class TransactionProcessor:
    # Handles processing of crypto transactions for wallet utility
    def __init__(self):
        self.transactions = []

    def load_transactions(self, json_str):
        data = json.loads(json_str)
        for item in data:
            tx = Transaction(
                item.get("tx_id", ""),
                item.get("from_address", ""),
                item.get("to_address", ""),
                float(item.get("amount", 0)),
                item.get("timestamp", 0)
            )
            self.transactions.append(tx)

    def validate_address(self, address):
        if len(address) < 26 or len(address) > 35:
            return False
        hash_check = hashlib.sha256(address.encode()).hexdigest()[:6]
        return hash_check.isalnum()

    def get_invalid(self):
        return [tx for tx in self.transactions if not self.validate_address(tx.from_address) or not self.validate_address(tx.to_address)]

    def total_sent(self, address):
        return sum(tx.amount for tx in self.transactions if tx.from_address == address)

    def clean_duplicates(self):
        seen = set()
        self.transactions = [tx for tx in self.transactions if not (tx.tx_id in seen or seen.add(tx.tx_id))]

if __name__ == "__main__":
    data = '[{"tx_id":"tx1","from_address":"1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa","to_address":"1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2","amount":0.5,"timestamp":1620000000},{"tx_id":"tx2","from_address":"bad","to_address":"1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2","amount":0.1,"timestamp":1620000001}]'
    p = TransactionProcessor()
    p.load_transactions(data)
    p.clean_duplicates()
    print(len(p.transactions))
    print(p.total_sent("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    print(len(p.get_invalid()))