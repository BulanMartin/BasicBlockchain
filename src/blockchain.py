import datetime
import json
import hashlib

class Blockchain:

    def __init__(self):

        # Initialize blockchain
        self.chain = []

        #Create first block
        self.create_block(nonce = 1, prev_hash = '0')

    # Create new block an append it to the chain
    def create_block(self, nonce, prev_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'prev_hash': prev_hash
                }

        self.chain.append(block)
        return block