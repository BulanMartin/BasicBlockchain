from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    prev_block = blockchain.get_prev_block()

    nonce = blockchain.proof_of_work(prev_block)
    prev_hash = blockchain.hash(prev_block, nonce)
    block = blockchain.create_block(nonce, prev_hash)

    response = {'Blockchain': 'New block was mined!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'nonce': block['nonce'],
                'previous_hash': block['prev_hash'],
                'current_complexity': block['current_complexity']}

    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}

    return jsonify(response), 200


@app.route('/complexity/', methods=['GET'])
@app.route('/complexity/<int:leading_zeros>', methods=['GET'])
def set_complexity(leading_zeros = None):

    if leading_zeros:
        blockchain.leading_zeros=leading_zeros

        response = {'Leading zeros set to ': blockchain.leading_zeros}
        return jsonify(response), 200

    else:

        response = {'Current number of leading zeros ': blockchain.leading_zeros}
        return jsonify(response), 200

@app.route('/validate', methods=['GET'])
def validate():

    response = {'Chain valid': blockchain.validate(blockchain.chain)}

    return jsonify(response), 200

app.run(host = '0.0.0.0', port = 5000)