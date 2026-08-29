# wallet-utility-13

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

wallet-utility-13 is a Python library for deriving and managing hierarchical deterministic cryptocurrency wallets. It enables developers to generate addresses across multiple blockchains from a single seed phrase while maintaining security best practices.

## Features
- Multi-coin support for Bitcoin, Ethereum, and Binance Smart Chain using standard BIP-44 paths
- Secure mnemonic-to-seed conversion with optional passphrase
- Address derivation for legacy, segwit, and native segwit formats
- Private key and public key export utilities

## Installation

```bash
git clone https://github.com/Developer/wallet-utility-13.git
cd wallet-utility-13
pip install -r requirements.txt
pip install -e .
```

## Usage

```python
from wallet_utility_13 import HDWallet

wallet = HDWallet.from_mnemonic("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about")

eth_address = wallet.get_address("ethereum", account=0, index=0)
print(eth_address)
```