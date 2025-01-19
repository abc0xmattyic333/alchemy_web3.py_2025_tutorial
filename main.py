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
    

# Get the latest transaction balance in wei

latest_transaction = web3.eth.get_transaction_by_block('latest', 0)
print(f"Latest Transaction: {latest_transaction}")

# Get the latest transaction receipt

latest_transaction_receipt = web3.eth.get_transaction_receipt(latest_transaction['hash'])
print(f"Latest Transaction Receipt: {latest_transaction_receipt}")

# Check the current gas price
gas_price = web3.eth.gas_price
print(f"Current Gas Price: {gas_price}")