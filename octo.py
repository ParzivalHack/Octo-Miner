from hashlib import sha256
from web3 import Web3
import os
import time
os.system("clear")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠓⠁⠀⠀⠀⠀⠐⠱⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⠷⠓⠑⠱⡳⣿⣿⣿⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠷⠓⠑⠱⡳⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⠃⢈⣬⣮⣌⠈⠐⠱⣷⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⡿⠳⠁⢀⣌⣮⣎⢈⠐⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⢨⣿⣿⣿⣿⣿⣎⠀⠀⠱⢄⠱⡧⡆⠀⠀⡤⡶⠓⡈⠓⠀⠀⣨⣿⣿⣿⣿⣿⢎⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⡷⠳⠳⠳⠳⠳⠳⠳⠣⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⠀⠲⠳⠳⠳⠳⠳⠳⠳⡷⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⠃⠀⢈⣌⣌⣌⢈⢈⢈⢈⢈⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⢈⢈⢈⢈⢈⣌⣌⣌⢈⠀⠰⣿⣿⣿⣿")
print("                 ⣿⣿⣿⠌⠀⣿⣿⣿⣿⣿⣿⣿⣿⠷⠁⠀⠀⣈⠌⠀⠀⣠⢌⠀⠀⠑⡳⣿⣿⣿⣿⣿⣿⣿⣿⠀⣀⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣯⢈⡳⣿⣿⣿⣿⣿⠷⠁⠀⢀⣬⣾⣿⠏⠀⠀⣰⣿⣯⣎⠈⠀⠐⡳⣿⣿⣿⣿⣿⠷⢈⣾⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣈⣮⣿⣿⣿⣿⠏⠀⠀⣰⣿⣿⣿⣿⣮⢌⠀⠐⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿")                                   
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠈⠀⡳⣿⣿⣿⣿⣿⣏⠀⠀⣾⣿⣿⣿⣿⣿⠷⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢈⠱⠳⣻⣿⣿⣿⠀⠀⣿⣿⣿⢿⠳⠓⢈⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠎⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
os.system("toilet Octo Miner")
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/97d9b42d4a4a4c0ca98ea173bdcf4250"))
print("Connected to Web3: ", web3.isConnected())
to_account = str(input("Import your wallet: "))
balance = web3.eth.get_balance(to_account)
print("Your current balance is 0.0",balance, "ETH.")
time.sleep(1)
difficulty = int(input("Choose difficulty (suggested 13 or above): "))
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined ETH with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    start = time.time()
    print("Started mining...")
    new_hash = mine(5, transactions, '0x0fc2008d1fc2ba5a41b61497f802b830a50c2ae2ba05cf9611545b72ebe1204f', difficulty)
    total_time = str((time.time() - start))
    print(f"Finished mining! Mining took: {total_time} seconds.")
    print("Hash mined is: ", new_hash) 
