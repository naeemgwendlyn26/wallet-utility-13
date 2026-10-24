from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Optional

class CryptoProcessor:
    """Handles precision formatting and normalization of crypto assets."""

    DEFAULT_PRECISION = 8

    @staticmethod
    def format_amount(amount: float, precision: int = DEFAULT_PRECISION) -> str:
        """Convert float amounts to consistent string representation."""
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a numeric type")
        
        factor = Decimal(10) ** -precision
        d_amount = Decimal(str(amount)).quantize(factor, rounding=ROUND_HALF_UP)
        return format(d_amount, f'f')

    @classmethod
    def normalize_tx_data(cls, data: Dict[str, any]) -> Dict[str, any]:
        """Sanitize transaction dictionary for backend persistence."""
        return {
            "tx_hash": str(data.get("hash", "")).lower(),
            "asset": str(data.get("symbol", "")).upper(),
            "value": cls.format_amount(float(data.get("amount", 0))),
            "timestamp": int(data.get("ts", 0))
        }

    @staticmethod
    def validate_asset_code(code: Optional[str]) -> bool:
        """Simple check for crypto asset ticker validity."""
        if not code or not isinstance(code, str):
            return False
        return 2 <= len(code) <= 10 and code.isalnum()