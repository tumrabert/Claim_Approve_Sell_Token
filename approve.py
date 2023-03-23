import os
from web3 import Web3


def approve_arb(arb_token_address, infura_url, uniswap_rounter_address, private_key, arb_token_abi, amount):
    # Connect to Arbitrum using Infura
    w3 = Web3(Web3.HTTPProvider(infura_url))

    # Initialize accounts and contracts
    account = w3.eth.account.privateKeyToAccount(private_key)
    arb_token = w3.eth.contract(
        address=arb_token_address, abi=arb_token_abi)

    # Approve ARB tokens
    amount = w3.toWei(amount, 'ether')
    spender = uniswap_rounter_address  # Uniswap router address
    approve_txn = arb_token.functions.approve(spender, amount).buildTransaction({
        'from': account.address, 'gas': 1000000})
    signed_txn = account.signTransaction(approve_txn)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return tx_hash.hex()
