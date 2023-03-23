import os
from web3 import Web3


def swap_arb(uniswap_rounter_address, arb_token_address, usdt_token_address, infura_url, private_key, uniswap_router_abi, amount):
    # Connect to Arbitrum using Infura
    w3 = Web3(Web3.HTTPProvider(infura_url))

    # Initialize accounts and contracts
    account = w3.eth.account.privateKeyToAccount(private_key)
    uniswap_router = w3.eth.contract(
        address=uniswap_rounter_address, abi=uniswap_router_abi)

    # Swap ARB tokens for USDT
    arb_token = arb_token_address
    # USDT token contract address on Arbitrum
    usdt_token = usdt_token_address
    amount_in = w3.toWei(amount, 'ether')
    min_out = 1  # Set a low value to execute the swap immediately
    # 20 minutes from the current block time
    deadline = w3.eth.getBlock('latest')['timestamp'] + 60 * 20
    path = [arb_token, usdt_token]

    swap_txn = uniswap_router.functions.swapExactTokensForTokens(
        amount_in,
        min_out,
        path,
        account.address,
        deadline
    ).buildTransaction({'from': account.address, 'gas': 250000})

    signed_txn = account.signTransaction(swap_txn)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return tx_hash.hex()
