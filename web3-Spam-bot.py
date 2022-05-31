import json
from web3 import Web3
import asyncio
import config
import time

sender_address ='0x'
contract_address = '0x768fd848a93AE495C42ce43cC776F3dDD0Ea3196'
refer_address = '0x1'
abi = [{"inputs":[{"internalType":"address","name":"_devFeeReceiver","type":"address"},{"internalType":"address","name":"_marketingFeeReceiver","type":"address"},{"internalType":"address","name":"_treasuryFeeReceiver","type":"address"}],"stateMutability":"payable","type":"constructor"},{"inputs":[],"name":"FeeTooLow","type":"error"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"OnlyOwner","type":"error"},{"inputs":[{"internalType":"uint256","name":"eth","type":"uint256"},{"internalType":"uint256","name":"contractBalance","type":"uint256"}],"name":"calculateDishesBuy","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"Dishes","type":"uint256"}],"name":"calculateDishesSell","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"ref","type":"address"}],"name":"cookDish","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"devourDishes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"dishRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"adr","type":"address"}],"name":"dishRewardsForAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"adr","type":"address"}],"name":"getChefsForAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"adr","type":"address"}],"name":"getDishesForAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMyChefs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMyDishes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"adr","type":"address"}],"name":"getPendingDishes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOpen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"ref","type":"address"}],"name":"makeChefs","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"openKitchen","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]

bsc = 'https://bsc-dataseed4.binance.org/'
bsc_chainID = "56"

poly = 'https://polygon-rpc.com'
poly_chainID = "137"

avax = "https://api.avax.network/ext/bc/C/rpc"
avax_chainID = "43114"

web3 = Web3(Web3.HTTPProvider(bsc)) #chain
print(web3.isConnected())

refer_address = web3.toChecksumAddress(refer_address)
sender_address = web3.toChecksumAddress(sender_address)
contract_address = web3.toChecksumAddress(contract_address)
contract = web3.eth.contract(address=contract_address, abi=abi)
nonce = web3.eth.get_transaction_count(sender_address)

def buy():
    nonce = web3.eth.get_transaction_count(sender_address)
    #Please edit the fucntion name based on the abi of the smart contract E.G. cookDish
    #You can edit the from, gas, gasPrice, value based on your setting
    txn = contract.functions.cookDish(
    refer_address,
    ).buildTransaction({
    'from': sender_address,
    'gas': 800000,
    'gasPrice': web3.toWei('10','gwei'),
    'value': web3.toWei('1.5','ether'),
    'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key="private key")
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Record: " + web3.toHex(tx_token))

while True:
    try:
        buy()
    except:
        print("Node has been sent")
