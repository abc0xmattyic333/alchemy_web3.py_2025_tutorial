# Install the Web3 library using pip

# Import the required libraries
from web3 import Web3

# Replace with your Alchemy API URL
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/iZafxHRZc-fNW3y7Uffo0fDZp26S6IKw"
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Check if connected
if web3.is_connected():
    print("Connected to Ethereum network")
    # Get the latest block number
    latest_block = web3.eth.block_number
    print(f"Latest Ethereum Block Number: {latest_block}")
else:
    print("Failed to connect to Ethereum network")
    