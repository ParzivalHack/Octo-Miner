from hashlib import sha256
from web3 import Web3
import os
os.system("toilet Octopus Miner")
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/97d9b42d4a4a4c0ca98ea173bdcf4250"))
print("Connected to Web3: ", web3.isConnected())
to_account = str(input("Import your wallet: "))
balance = web3.eth.get_balance(to_account)
print("Your current balance is", balance, "ETH.")
sleep 1
difficulty = int(input("Choose difficulty (suggested 13): "))
private_key = str(input("Import your private key to access your wallet: ")
address1 = Web3.toChecksumAddress(to_account)
nonce =web3.eth.getTransactionCount(address19
TX = {
    'nonce': nonce,
    'to': address1,
    'value': web3.toWei(0.001, 'ether'),
    'gas': 21000
    'gasPrice': web3.toWeì(40, 'gwel')
}
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_transaction = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
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
    import time
    start = time.time()
    print("Started mining...")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"Finished mining! Mining took: {total_time} seconds.")
    print(new_hash) 
