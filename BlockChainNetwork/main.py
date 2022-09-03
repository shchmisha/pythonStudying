import json
import os
import random
import threading
from BlockChainNetwork.BlockChainNode.wallet.wallet import Wallet
from flask import Flask, jsonify, request
from BlockChainNetwork.sockets.socketServer import SocketServer
from threading import Thread

app = Flask(__name__)
PORT = 5000

networks = {}

@app.route('/blockchain/generate')
def generate_network():
    # wallet = Wallet()
    port = random.randint(8000,9000)
    host = 'localhost'
    network = SocketServer(host, port)
    networks[port] = network
    print(networks)
    # return jsonify({'eccPrivateKey': wallet.privateKey, 'eccPublicKey': wallet.publicKey,  'port': port})
    return jsonify({'port': port})

@app.route('/blockchain/get_chain', methods=['POST'])
def route_blockchain():
    port = request.get_json()['port']
    return jsonify(networks[port].get_chain())

@app.route('/blockchain/upload', methods=['POST'])
def route_upload_document():
    documentData = request.get_json()
    port = documentData['port']
    publicKey = documentData['document']['publicKey']
    data = documentData['document']['data']
    signature = documentData['document']['signature']
    networks[port].upload_document({'address': publicKey, 'data': data, 'signature': signature})

app.run(port=PORT)



