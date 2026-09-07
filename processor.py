import re

def truncate_address(address: str, start_chars: int = 6, end_chars: int = 4) -> str:
    """Safely truncates a crypto address for user interface display."""
    if not address or len(address) <= (start_chars + end_chars):
        return address
    return f"{address[:start_chars]}...{address[-end_chars:]}"

def wei_to_ether(wei: int) -> float:
    """Converts a value in Wei to Ether."""
    return float(wei) / 10**18

def ether_to_wei(ether: float) -> int:
    """Converts a value in Ether to Wei."""
    return int(ether * 10**18)

def process_transaction_input(tx_data: dict) -> dict:
    """Processes and standardizes raw transaction data for wallet display."""
    processed = {}
    
    raw_to = tx_data.get("to", "")
    processed["to_address"] = str(raw_to).strip()
    processed["to_display"] = truncate_address(processed["to_address"])
    
    raw_value = tx_data.get("value", 0)
    try:
        wei_val = int(raw_value)
    except (ValueError, TypeError):
        wei_val = 0
        
    processed["value_wei"] = wei_val
    processed["value_ether"] = wei_to_ether(wei_val)
    
    gas_price = int(tx_data.get("gasPrice", 0))
    gas_limit = int(tx_data.get("gas", 0))
    processed["fee_wei"] = gas_price * gas_limit
    processed["fee_ether"] = wei_to_ether(processed["fee_wei"])
    
    return processed