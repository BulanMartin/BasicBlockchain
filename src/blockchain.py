import datetime
import hashlib
import json

class Blockchain:

    def __init__(self):
        self.chain = []
        self.leading_zeros = 4
        self.create_block(nonce = 1, prev_hash = '0')
        
    def create_block(self, nonce, prev_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'prev_hash': prev_hash,
                 'current_complexity': self.leading_zeros
                }

        self.chain.append(block)
        return block

    def get_prev_block(self):
        return self.chain[-1]

    def proof_of_work(self, prev_block):
        nonce = 1
        check_nonce = False
        while check_nonce == False:
            hash_operation = hashlib.sha256(json.dumps(str(prev_block) + str(nonce), sort_keys=True).encode()).hexdigest()

            if hash_operation[:self.leading_zeros] == self.leading_zeros*'0':
                check_nonce = True
            else:
                nonce += 1

        return nonce

    def hash(self, prev_block, nonce):
        
        return hashlib.sha256(json.dumps(str(prev_block) + str(nonce), sort_keys=True).encode()).hexdigest()


    def validate(self, chain):

        prev_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['prev_hash'] != self.hash(prev_block, block['nonce']):

                return False

            nonce = block['nonce']
            hash_operation = hashlib.sha256(json.dumps(str(prev_block) + str(nonce), sort_keys=True).encode()).hexdigest()

            if hash_operation[:block['current_complexity']] != block['current_complexity']*'0':

                return False

            prev_block = block
            block_index += 1

        return True

