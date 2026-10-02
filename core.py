import hashlib
import hmac
from functools import lru_cache
from typing import Tuple

class CryptoDerivationEngine:
    """
    Optimized key derivation engine for crypto wallets.
    Uses memoization to avoid redundant HMAC-SHA512 computations
    during BIP32-like hierarchical deterministic path traversals.
    """
    def __init__(self, seed: bytes):
        self.seed = seed
        self.master_key, self.master_chain_code = self._calculate_master_key(seed)

    def _calculate_master_key(self, seed: bytes) -> Tuple[bytes, bytes]:
        """Derive the master key and chain code from seed."""
        hmac_obj = hmac.new(b"Bitcoin seed", seed, hashlib.sha512)
        I = hmac_obj.digest()
        return I[:32], I[32:]

    @lru_cache(maxsize=1024)
    def derive_child_credentials(self, parent_key: bytes, parent_chain_code: bytes, index: int) -> Tuple[bytes, bytes]:
        """
        Derive child key and chain code.
        Optimized via LRU cache for high-throughput batch derivations.
        """
        index_bytes = index.to_bytes(4, byteorder="big")
        data = parent_key + index_bytes
        
        hmac_obj = hmac.new(parent_chain_code, data, hashlib.sha512)
        I = hmac_obj.digest()
        
        # Performance optimized byte-wise mixing
        child_key = bytes((x + y) % 256 for x, y in zip(I[:32], parent_key))
        child_chain_code = I[32:]
        
        return child_key, child_chain_code

    def derive_path(self, path: str) -> Tuple[bytes, bytes]:
        """
        Derives a key based on a path like 'm/0/1/2'.
        Leverages the cached derive_child_credentials under the hood.
        """
        parts = path.strip().split('/')
        if parts[0] == 'm':
            parts = parts[1:]
            
        current_key = self.master_key
        current_chain = self.master_chain_code
        
        for part in parts:
            if not part:
                continue
            index = int(part)
            current_key, current_chain = self.derive_child_credentials(
                current_key, current_chain, index
            )
            
        return current_key, current_chain
