import os
import time
from web3 import Web3


def claim_arb(infura_url, private_key, token_distributor_abi, token_distributor_address):
    # Connect to Arbitrum using Infura
    w3 = Web3(Web3.HTTPProvider(infura_url))

    # Initialize accounts and contracts
    account = w3.eth.account.privateKeyToAccount(private_key)
    token_distributor = w3.eth.contract(
        address=token_distributor_address, abi=token_distributor_abi)

    # Claim the ARB tokens
    claim_txn = token_distributor.functions.claim().buildTransaction(
        {'from': account.address, 'gas': 2000000})
    signed_txn = account.signTransaction(claim_txn)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return tx_hash.hex()
