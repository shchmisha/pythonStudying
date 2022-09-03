import json
import random
import socket
import threading
import time
from BlockChainNetwork.BlockChainNode.server.socketClient import BlockchainNode

# dont store chain in the root
# whenever a request to get the chain is made,make a call to the other nodes and get their chain

class SocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((host, port))
        print("server initialized")
        self.clients = {}
        self.chain = []
        self.block = {}
        self.start_network()

    def start_server(self):
        self.sock.listen()
        while True:
            # establish connection with client
            conn, addr = self.sock.accept()

            print('Connected to :', addr[0], ':', addr[1])

            # Start a new thread and return its identifier
            # start_new_thread(handle_clients, (conn, addr))
            thread = threading.Thread(target=self.handle_clients, args=(conn, addr))
            thread.start()
        self.sock.close()

    def handle_clients(self, conn, addr):
        print("new client connected ", addr)
        # conn.send(json.dumps({'route': 'replace_data', 'chain': self.chain, 'pool': self.documentPool}).encode('utf-8'))
        if self.clients != {}:
            list(self.clients.values())[random.randint(0, len(list(self.clients.values()))-1)].send(json.dumps({'route': 'get_data', 'port': addr[1]}).encode('utf-8'))
        self.clients[addr[1]] = conn
        while True:
            dataJson = conn.recv(4096).decode('utf-8')
            if not dataJson:
                print("client disconnected: "+str(addr[1]))
                del self.clients[addr[1]]
                break
            data = json.loads(dataJson)
            if data['route'] == 'new_block':
                data['route'] = 'add_block'
                for client in list(self.clients.values()):
                    if client != conn:
                        client.send(json.dumps(data).encode('utf-8'))
            elif data['route'] == 'new_document':
                document = data['content']
                # self.documentPool.append(document)
                data['route'] = 'add_document'
                for client in list(self.clients.values()):
                    if client != conn:
                        client.send(json.dumps(data).encode('utf-8'))
            elif data['route'] == 'sync':
                self.channels[random.randint(0, len(list(self.clients.values()))-1)].send(json.dumps({'route': 'get_data', 'port': addr[1]}).encode('utf-8'))
            elif data['route'] == 'send_data':
                clientPort = data['content']['port']
                print(clientPort)
                self.clients[clientPort].send(json.dumps({'route': 'replace_data', 'chain': data['content']['chain'], 'pool': data['content']['pool']}).encode('utf-8'))
            elif data['route'] == 'send_chain':
                self.chain = data['chain']
            elif data['route'] == 'send_block':
                print(data['block'])
                self.block = data['block']
        conn.close()

    def broadcast(self, conn, data):
        for client in self.clients.values():
            if client != conn:
                client.send(json.dumps(data).encode('utf-8'))

    def mineBlocks(self):
        while True:
            if self.clients != {}:
                list(self.clients.values())[random.randint(0, len(self.clients)-1)].send(json.dumps({'route': 'mine_block'}).encode('utf-8'))
            time.sleep(30.0)

    def start_network(self):
        self.server_thread = threading.Thread(target=self.start_server)
        self.mine_thread = threading.Thread(target=self.mineBlocks)
        self.mine_thread.start()
        self.server_thread.start()
        self.create_nodes(2)

    def create_nodes(self, n):
        for i in range(n):
            BlockchainNode(self.host, self.port)

    def upload_document(self, documentData):
        data = {'route': 'upload_document', 'content': {'address': documentData['address'], 'data': documentData['data'], 'signature': documentData['signature']}}
        print(list(self.clients.values())[random.randint(0, len(self.clients)-1)])
        list(self.clients.values())[random.randint(0, len(self.clients)-1)].send(json.dumps(data).encode('utf-8'))

    def get_chain(self):
        list(self.clients.values())[random.randint(0, len(self.clients)-1)].send(json.dumps({'route': 'get_chain'}).encode('utf-8'))
        time.sleep(15)
        return self.chain
        # return jsonify(document.to_json())

# server = SocketServer('localhost', 8080)
# server.create_nodes(2)