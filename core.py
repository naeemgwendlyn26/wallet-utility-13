import hashlib
from functools import lru_cache
from typing import List, Dict

class CoreWallet:
    def __init__(self):
        self._balance_cache: Dict[str, float] = {}
        self._tx_cache: Dict[str, Dict] = {}

    @lru_cache(maxsize=512)
    def _compute_hash(self, data: str) -> str:
        # Optimized hash computation with lru cache
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def get_balance(self, address: str) -> float:
        # Use cache to avoid recomputation
        if address in self._balance_cache:
            return self._balance_cache[address]
        addr_hash = self._compute_hash(address)
        # Derive pseudo balance from hash for demo
        balance = int(addr_hash[:16], 16) / 1e12
        self._balance_cache[address] = balance
        return balance

    def batch_get_balances(self, addresses: List[str]) -> Dict[str, float]:
        # Batch processing to minimize cache misses
        results: Dict[str, float] = {}
        uncached = []
        for address in addresses:
            if address in self._balance_cache:
                results[address] = self._balance_cache[address]
            else:
                uncached.append(address)
        for address in uncached:
            results[address] = self.get_balance(address)
        return results

    def process_payment(self, address: str, amount: float) -> Dict:
        tx_key = f"{address}:{amount}"
        if tx_key in self._tx_cache:
            return self._tx_cache[tx_key]
        balance = self.get_balance(address)
        if balance < amount:
            result = {"status": "insufficient", "balance": balance}
        else:
            new_balance = balance - amount
            self._balance_cache[address] = new_balance
            result = {"status": "success", "new_balance": new_balance}
        self._tx_cache[tx_key] = result
        return result

    def get_transaction_history(self, address: str) -> List[Dict]:
        history = []
        for key, res in self._tx_cache.items():
            if key.startswith(address):
                history.append(res)
        return history

    def clear_caches(self) -> None:
        self._balance_cache.clear()
        self._tx_cache.clear()
        self._compute_hash.cache_clear()