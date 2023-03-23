# Claim_Approve_Sell_Token

## Installation

1.Install all dependencies
using this command

```bash
python install_dependencies.py
```

2.Create file .env.local to save key in your local

(fill your key in ...)

```bash
PRIVATE_KEY=...
INFURA_PROJECT_URL=...
ARBISCAN_API_KEY=...
ARB_TOKEN_ADDRESS='0x912ce59144191c1204e64559fe8253a0e49e6548'
UNISWAP_ROUTER_ADDRESS='0xE592427A0AEce92De3Edee1F18E0157C05861564'
USDT_ADDRESS='0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'
ARB_TOKEN_DISTRIBUTOR_ADDRESS='0x67a24ce4321ab3af51c2d0a4801c3e111d88c9d9'
```

every value is string

3.Run main file by

```bash
python main.py
```

I set countdown by UNIXTIMESTAMP
when time is out.

It will do claim approve and swap.

Get your own timestamp from this website
https://www.unixtimestamp.com/
