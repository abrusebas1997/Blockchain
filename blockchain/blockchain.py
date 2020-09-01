import hashlib
import json
from time import time

# Creating the app node

app = Flask(__name__)
node_identifier = str(uuid4()).replace(‘-‘,”)

# Initializing blockchain

blockchain = Blockchain()

@app.route(‘/mine’, methods=[‘GET’])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block[‘proof’]
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender = '0',
        recipient = node_identifier,
        amount = 1,
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    response = {
        'message':'The new block has been forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash' : block['previous_hash']
    }

    return jsonify(response), 200


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


    @app.route(‘/transactions/new’, methods=[‘POST’])
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

    @app.router(‘/chain’, methods=[‘GET’])
    def full_chain():
        response = {
            'chain':blockchain.chain,
            'length':len(blockchain.chain)
        }

        return jsonify(response), 200

    if __name__ == ‘__main__’:
        app.run(host=“0.0.0.0”, port=5000)

    @staticmethod
    def hash(block):
        #Used for hashing a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        return self.chain[-1]
