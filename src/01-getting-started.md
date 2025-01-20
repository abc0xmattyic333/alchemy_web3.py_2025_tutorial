# Getting Started

The first thing you are going to want to do is install Python on your local computer.

You can do so by going to [Python](https://www.python.org/).

Click download, and install depending on the system you need. I am on windows, and have it already installed.

You can check to see if you have python installed by going to your terminal and typing:

```
python3
```

You can see that I have it installed on my computer by visiting the images folder.

Create a working directory by typing this command in.

```
mkdir alchemy_web3.py_2025_tutorial
```

The next thing you are going to want to do is choose a text editor or a IDE to open our working directory.

I am going to be using VS Code throughout this tutorial.

You can install VS Code by going to the following link:
[VS Code](https://code.visualstudio.com/)

After you have python installed, and an editor or IDE of your choosing installed open the working directory inside of it.

I can open VS Code from my terminal with the following command:

```
code .
```

Once you have your editor or IDE open you can then create a new venv. Choose the python interpreter.

Create a new python file:

```
main.py
```

You will want to install the Web3 library by typing this command into your terminal:

```
pip install Web3
```

Now, you will want to visit Alchemy and create a free account. [Alchemy](https://www.alchemy.com/)

After you setup a free account you then will be introduced to the Alchemy Dashboard.

You will want to create a new API key here, for our new project.

Go back to your main.py file and type in the following code:

```
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
    
```

***Replace With Your Alchemy API Key*** 

_Run your main.py file_

You should see the output is connected to _Ethereum Mainnet_ and the _latest blockchain number_.

Let's check out our Alchemy Dashboard to view our _Analytics_ to see if we were successful.

We will also verify the block number using [Etherscan](https://etherscan.io/)

I suggest running the program again to see the latest block number to just be sure.

You can verify that the output of the block is indeed on Etherscan.io by copying the block number and searching it in the search bar on [Etherscan](https://etherscan.io/).

Now let's try to get some more data from the blockchain.

You can see that I have updated our main.py file and added the following code:

```
latest_transaction = web3.eth.get_transaction_by_block('latest', 0)
print(f"Latest Transaction: {latest_transaction}")

# Get the latest transaction receipt

latest_transaction_receipt = web3.eth.get_transaction_receipt(latest_transaction['hash'])
print(f"Latest Transaction Receipt: {latest_transaction_receipt}")

# Check the current gas price
gas_price = web3.eth.gas_price
print(f"Current Gas Price: {gas_price}")
```

If you go to the images folder, you will see the latest transaction and latest transaction receipt as well as the current gas price.

What if we wanted to check some different on-chain data from say Flow, or other EVM's?

We can first replace our Alchemy API Key with the Network that we would like to get some data from.

I am going to use Flow, I think Flow has a lot of upscale and it's still relatively new within the Blockchain space.

It is also a cheaper alternative to use for beginners due to the current gas fees on Ethereum, Solana, or other chains. 

To learn more about Flow and how to get started developing on Flow, visit the following link(s). 

[Flow](https://flow.com/)

[Flow Github](https://github.com/onflow)

[Flow Playground](https://play.flow.com/)

[Emerald Academy](https://academy.ecdao.org/en?utm_source=Flowverse&utm_medium=Website&utm_campaign=Dapp)

[Emerald Dao Github](https://github.com/emerald-dao)

[Flow Wallet](https://wallet.flow.com/)

[Flowverse](https://www.flowverse.co/)

[Cadence](https://cadence-lang.org/docs)

[Cadence Cookbook](https://cadence-cookbook.vercel.app/?utm_source=Flowverse&utm_medium=Website&utm_campaign=Dapp)

[CadenceFun](https://cadence-fun-frontend.vercel.app/?utm_source=Flowverse&utm_medium=Website&utm_campaign=Dapp)

Alright, there are several ways that we can go about obtaining some Flow EVM data.

- 1. We could create an entirely new working directory using the same methods as before...
- 2. Or we could just replace our Alchemy API Key with the Flow EVM Mainnet endpoint and modify our main.py file to see the changes.

You can replace the code in your main.py file with the following code:
```
# Install the Web3 library using pip

# Import the required libraries
from web3 import Web3

# Replace with your Alchemy API URL
alchemy_url = "https://flow-mainnet.g.alchemy.com/v2/iZafxHRZc-fNW3y7Uffo0fDZp26S6IKw"
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Check if connected
if web3.is_connected():
    print("Connected to Flow network")
    # Get the latest block number
    latest_block = web3.eth.block_number
    print(f"Latest Flow Block Number: {latest_block}")
else:
    print("Failed to connect to Flow network")
    

# Check the current gas price
gas_price = web3.eth.gas_price
print(f"Current Gas Price: {gas_price}")
```
You should get an output that you are connected to Flow Mainnet, the latest block number, and the current gas price.

If you take a look in our images folder you will see the output of my Python program.

Now, head back to our Alchemy Dashboard to view our analytics.

You should see that I have a total of 12 requests.

You can also check the HTTPS Request Count By Network, you will see the graph has updated to display that we have connected to Flow EVM mainnet.

You then can go back to our request logs, and see eth_gasPrice, eth_blockNumber, web3_clientVersion calls were made to the flow evm.

Awesome! :)