from BLinked.demoCheck.merkletools import MerkleTools
import os
import csv

from web3 import Web3
import json
from BLinked.demoCheck.contract_abi import abi

universities = ['VJTI', 'IITB', 'KJSCE']

# Merkle Tree init
mt = MerkleTools(hash_type='sha3_256')
count = 0
filename = 'VJTI_2016.csv'

institute = "VJTI"

with open(os.path.join('certificate', filename)) as File:
    reader = csv.reader(File)
    for row in reader:
        # studentID CPI Name batch college
        data = str(row[0]) + str(row[2]) + str(row[1]) + str(row[3]) + institute
        batch = str(row[3])
        mt.add_leaf(data, do_hash=True)
        count += 1

mt.make_tree()



# if mt.get_leaf_count() != count:
# print("not equal")
# print(count, mt.get_leaf_count())
if mt.get_tree_ready_state:
    merkleRoot = mt.get_merkle_root()


CONTRACT_ADDR = '0x92a4f363725DfaF16756Ef6352033cEF8C24F708'
WALLET_PRIVATE_KEY = '00fc171a1df903ad3c5840c8201c670ca7d8ac81d6b6f8ea90cfe6c54984af44'
WALLET_ADDRESS = '0x3441B63fbAcb69Dca61780AECA639405a47DBe8A'

ganache_url = "http://127.0.0.1:7545"
registeredInstitutes = {"VJTI": 1, "KJSCE": 2, "IITB": 3}


class Blockchain:
    def __init__(self, institute):
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        self.institute = institute


        self.contract = self.web3.eth.contract(address=CONTRACT_ADDR, abi=abi)

        self.web3.eth.defaultAccount = self.web3.eth.accounts[1]
        print("Connected to blockchain with account", self.web3.eth.defaultAccount)

    def addBatchMerkleRoot(self, batch, batchMerkleRoot):
        self.contract.functions.addBatchMerkleRoot(self.institute, batch, batchMerkleRoot).transact()

    def verifyBatchMerkleRoot(self, institute, batch, batchMerkleRoot):
        return self.contract.functions.verifyBatchMerkleRoot(institute, batch, batchMerkleRoot).call()


bc = Blockchain(institute)
print("Adding to the blockchain: ", batch, merkleRoot)
try:
    bc.addBatchMerkleRoot(batch, merkleRoot)
    print("successfully added")
except:
    print("Institute not registered!")

itr = 0
with open(os.path.join('certificate', filename)) as File:
    reader = csv.reader(File)
    for row in reader:
        data = {}
        data["cpi"] = str(row[2])
        data["name"] = str(row[1])
        data["year"] = str(row[3])
        data["studentId"] = str(row[0])
        data["institution"] = institute
        data["merklePath"] = mt.get_proof(itr)
        itr += 1

        filename = str(row[1]) + '.json'

        with open(os.path.join('json', filename), 'w') as json_file:
            json_file.write(json.dumps(data))
    print("successfully generated the receipts and added to block chain")
