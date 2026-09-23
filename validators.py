import re
from functools import lru_cache
import hashlib

# Pre-compiled regex patterns for bitcoin and ethereum formats
BTC_LEGACY_RE = re.compile("^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")
BTC_BECH32_RE = re.compile("^bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39,59}$")
ETH_RE = re.compile("^0x[a-fA-F0-9]{40