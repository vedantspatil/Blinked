from web3 import Web3
import json
from .contract_abi import abi


CONTRACT_ADDR = '0x92a4f363725DfaF16756Ef6352033cEF8C24F708'
WALLET_PRIVATE_KEY = '00fc171a1df903ad3c5840c8201c670ca7d8ac81d6b6f8ea90cfe6c54984af44'
WALLET_ADDRESS = '0x3441B63fbAcb69Dca61780AECA639405a47DBe8A'

ganache_url = "http://127.0.0.1:7545"

class Blockchain:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))

        self.contract = self.web3.eth.contract(address=CONTRACT_ADDR, abi=abi)

        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        print("Connected to blockchain with default account", self.web3.eth.defaultAccount)

    def verifyBatchMerkleRoot(self, institute, batch, batchMerkleRoot):
        return self.contract.functions.verifyBatchMerkleRoot(institute, batch, batchMerkleRoot).call()



if __name__ == "__main__":
    bc = Blockchain()
    res = bc.verifyBatchMerkleRoot("VJTI", "2020", "0x14a6b49F7e3c04503A7b31DA4Abb4808c4d5E1Ac")
    print(res)