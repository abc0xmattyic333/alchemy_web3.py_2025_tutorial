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