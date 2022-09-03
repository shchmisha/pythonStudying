import json
import os
import random
import requests
from flask import Flask, jsonify, request
from src.wallet.wallet import Wallet
from src.blockchain.blockchain import Blockchain

data_pool = []

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine', methods=['POST'])
def route_mine():
    if data_pool == []:
        return jsonify({'empty': 'no data inside pool'})
    for i in range(len(data_pool)):
        block = blockchain.add_block(data_pool[i]['data'], data_pool[i]['wallet_addr'])
    return jsonify(block.to_json())

@app.route('/blockchain/upload', methods=['POST'])
def route_mine_block(): # this route should only be used for dev, PRIVATE KEY SHOULD NEVER BE CHANGED
    block_data = request.get_json() # request should contain the data wanted and the private key
    private_key = block_data['private_key']
    
    # if block_data['data'] and block_data['wallet_addr']:
    #     data_pool.append(block_data)
    #     return jsonify({'message': 'successfully added data to pool'})
    # return jsonify({'error': 'could not add data to pool'})
    


@app.route('/wallet/new')
def route_new_wallet():
    wallet = Wallet()
    try:
        private_key = wallet.private_key
        print(private_key)
        public_key =  wallet.public_key
        print(public_key)
        return jsonify({'private_key': private_key, 'public_key': public_key})
    except:
        return jsonify({'error': 'somethingisnt right'})



ROOT_PORT = 5000
PORT = ROOT_PORT

app.run(port=PORT)