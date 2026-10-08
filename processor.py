import json
import time
import logging
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logger = logging.getLogger("wallet_processor")

class NetworkProcessor:
    """Handles resilient JSON-RPC interactions with crypto nodes."""

    def __init__(self, endpoint: str, max_retries: int = 3, backoff_factor: float = 1.0):
        self.endpoint = endpoint
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def send_rpc_request(self, method: str, params: list) -> dict:
        """Sends a JSON-RPC payload with exponential backoff retry mechanism."""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        data = json.dumps(payload).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        req = Request(self.endpoint, data=data, headers=headers, method="POST")

        last_exception = None
        for attempt in range(self.max_retries + 1):
            try:
                with urlopen(req, timeout=10) as response:
                    return json.loads(response.read().decode("utf-8"))
            except (URLError, HTTPError) as err:
                last_exception = err
                if attempt == self.max_retries:
                    break
                
                sleep_time = self.backoff_factor * (2 ** attempt)
                logger.warning(
                    f"Request failed ({err}). Retrying in {sleep_time:.1f}s... "
                    f"({attempt + 1}/{self.max_retries})"
                )
                time.sleep(sleep_time)

        raise ConnectionError(f"RPC connection failed after {self.max_retries} retries: {last_exception}")