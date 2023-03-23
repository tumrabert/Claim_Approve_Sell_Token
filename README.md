# Claim_Approve_Sell_Token
##1.Install all dependencies
using this command

'''python install_dependencies.py'''

##2.Create file .env.local to save key in your local3
'''
PRIVATE_KEY=...
INFURA_PROJECT_URL=...
ARBISCAN_API_KEY=...
ARB_TOKEN_ADDRESS=...
UNISWAP_ROUTER_ADDRESS=...
USDT_ADDRESS=...
ARB_TOKEN_DISTRIBUTOR_ADDRESS=...
'''

every value is string

##3.Run main file
'''python main.py'''
I set countdown by UNIXTIMESTAMP
when time is out.
It will do claim approve and swap.

Get your own timestamp from this website 
https://www.unixtimestamp.com/
