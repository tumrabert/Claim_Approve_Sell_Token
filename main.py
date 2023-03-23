import os
import json
from dotenv import load_dotenv
from claim import claim_arb
from approve import approve_arb
from swap import swap_arb
from timecount import countdown


if __name__ == "__main__":
    load_dotenv('.env.local')
    print("this")

    infura_url = os.getenv('INFURA_PROJECT_URL')
    private_key = os.getenv('PRIVATE_KEY')

    token_distributor_address = os.getenv('ARB_TOKEN_DISTRIBUTOR_ADDRESS')
    arb_token_address = os.getenv('ARB_TOKEN_ADDRESS')
    uniswap_rounter_address = os.getenv('UNISWAP_ROUTER_ADDRESS')
    usdt_token_address = os.getenv('USDT_ADDRESS')

    # token_distributor_abi = json.load(os.getenv('TOKEN_DISTRIBUTOR_ABI'))
    # uniswap_router_abi = json.load(os.getenv('UNISWAP_ROUTER_ABI'))
    # arb_token_abi = json.load(os.getenv('ARB_TOKEN_ABI'))
    with open('json/UNISWAP_ROUNTER_ABI.json', 'r') as f:
        json_string = f.read()
    uniswap_router_abi = json.loads(json_string)

    with open('json/TOKEN_DISTRIBUTOR_ABI.json', 'r') as f:
        json_string = f.read()
    token_distributor_abi = json.loads(json_string)

    with open('json/ARB_TOKEN_ABI.json', 'r') as f:
        json_string = f.read()
    arb_token_abi = json.loads(json_string)

    claim_time = 1679576099  # in unix timestamp

    # Wait until the specified claiming time
    countdown(claim_time)

    claim_tx_hash = claim_arb(
        infura_url, private_key, token_distributor_abi, token_distributor_address)
    print(f"Claim TX Hash: {claim_tx_hash}")

    approve_tx_hash = approve_arb(
        arb_token_address, uniswap_rounter_address, infura_url, private_key, arb_token_abi, 5000)
    print(f"Approve TX Hash: {approve_tx_hash}")

    swap_tx_hash = swap_arb(uniswap_rounter_address, arb_token_address, usdt_token_address,
                            infura_url, private_key, uniswap_router_abi, 5000)
    print(f"Swap TX Hash: {swap_tx_hash}")
