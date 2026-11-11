# wallet-utility-13

A high-performance Python toolkit designed for streamlined cryptocurrency wallet management and derivation. This utility simplifies the process of generating, securing, and tracking multi-chain addresses for developers and power users.

## Features

*   **BIP-39 Implementation:** Securely generate and recover 12-to-24 word mnemonic phrases with full entropy validation.
*   **Multi-Chain Support:** Native derivation support for Bitcoin (BTC), Ethereum (ETH), and Solana (SOL) key pairs.
*   **Encrypted Storage:** Built-in AES-256 encryption module to protect local keystore files from unauthorized access.
*   **Balance Monitoring:** Lightweight integration with public blockchain explorers to fetch real-time address balances via API.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and set up your virtual environment:

```bash
git clone https://github.com/Developer/wallet-utility-13.git
cd wallet-utility-13
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Basic Usage

Generate a new Ethereum wallet and export the private key securely:

```python
from wallet_utility import WalletManager

# Initialize the manager
manager = WalletManager(chain="ETH")

# Create a new wallet
wallet = manager.generate_wallet()

# Save with password-based encryption
manager.save_to_disk(wallet, password="super-secret-password")

print(f"Address: {wallet.address}")
print(f"Private Key exported to keystore.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Distributed under the MIT License. See `LICENSE` for more information.*