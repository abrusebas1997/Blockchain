import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #This function creates new blocks and then adds to the existing chain
        self.new_block(previous_hash=1, proof=100)

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
        pass

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        pass
