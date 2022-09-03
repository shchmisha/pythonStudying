import json
import os
import random
import threading

from BlockChainNetwork.BlockChainNode.wallet.wallet import Wallet
from BlockChainNetwork.BlockChainNode.blockchain.blockchain import Blockchain
from BlockChainNetwork.BlockChainNode.blockchain.block import Block
from BlockChainNetwork.BlockChainNode.documents.documentPool import DocumentPool
from BlockChainNetwork.BlockChainNode.documents.document import Document
import socket
from threading import Thread

class BlockchainNode:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))
        self.blockchain = Blockchain()
        self.documentPool = DocumentPool()
        self.start_node()

    def network_listener(self):

        while True:
            print(threading.active_count())
            jsonData = self.sock.recv(4096).decode('utf-8')
            data = json.loads(jsonData)
            print(data)
            if data['route'] == 'add_block':
                blockJson = data['content']
                block = Block.from_json(blockJson)
                if(self.blockchain.addNewBlock(block)):
                    print("valid block")
                #     emit event saying block is valid
                #     in the root server, check the responses. if a response comes back telling therre is a corrupt block, it is synced witht he root state
                # find a way to make sure the root server can request a chain from a node
                else:
                    print("corrupt block")
            elif data['route'] == 'add_document':
                documentJson = data['content']
                document = Document.from_json(documentJson)
                if(self.documentPool.setDocument(document)):
                    print("valid doc")
                else:
                    print("corrupt doc")
            elif data['route'] == 'replace_data':
                chain = data['chain']
                pool = data['pool']

                newChain = Blockchain.from_json(chain)
                print([block.to_json() for block in newChain])
                self.blockchain.replaceChain(newChain)
                newPool = DocumentPool.from_json(pool)
                self.documentPool.setMap(newPool)
            elif data['route'] == 'mine_block':
                validDocuments = DocumentPool.validDocuments(self.documentPool.documentMap)
                print(validDocuments)

                block = self.blockchain.addBlock(validDocuments)
                self.documentPool.clearBlockchainDocuments(self.blockchain.chain)

                dataToSend = {'route': 'new_block', 'content': {'timestamp': block.timestamp, 'lastHash': block.lastHash, 'data': block.data, 'hash': block.hash}}
                self.sock.send(json.dumps(dataToSend).encode('utf-8'))
            elif data['route'] == 'upload_document':
                documentJson = data['content']
                document = Document.from_json(documentJson)
                if(self.documentPool.setDocument(document)):
                    print("valid doc")
                else:
                    print("corrupt doc")

                dataToSend = {'route': 'new_document', 'content': {'publicKey': document.publicKey, 'data': document.data, 'signature': document.signature, 'id': document.id}}
                self.sock.send(json.dumps(dataToSend).encode('utf-8'))
            elif data['route'] == 'get_data':
                # random client will receive a message to send their chain and pool over with a specified port number
                # this client will send their chain and when the message is recieved by the root it will send this chain to the required client, replacing their chain
                port = data['port']
                dataToSend = {'route': 'send_data', 'content': {'port': port, 'chain': self.blockchain.to_json(),'pool': self.documentPool.to_json()}}
                self.sock.send(json.dumps(dataToSend).encode('utf-8'))
            elif data['route'] == 'get_chain':
                dataToSend = {'route': 'send_chain', 'chain': self.blockchain.to_json()}
                self.sock.send(json.dumps(dataToSend).encode('utf-8'))
        sock.close()

    def start_node(self):
        self.node_thread = Thread(target=self.network_listener)
        self.node_thread.start()






