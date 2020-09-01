import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof +=1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f’{last_proof}{proof}‘.encode()
        guess_hash = hashlib.sha256(guess).hexigest()
        return guess_hash[:4] == “0000”

    def new_block(self, proof, previous_hash=None):
        #This function creates new blocks and then adds to the existing chain
        block = {
           'index': len(self.chain) + 1,
           'timestamp' : time(),
           'proof': proof,
           'previous_hash': previous_hash or self.hash(self.chain[-1]),
       }

   # Set the current transaction list to empty.

   self.current_transactions=[]
   self.chain.append(block)
   return block

    def new_transaction(self):
        #This function adds a new transaction to already existing transactions
        self.current_transactions.append(
            {
                'sender':sender,
                'recipient':recipient,
                'amount':amount,
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #Used for hashing a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        return self.chain[-1]
