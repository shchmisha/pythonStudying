from time import time_ns
from src.util.cryptoHash import cryptoHash
from src.util.config import GENESIS_DATA

class Block: 
    def __init__(self, timestamp, lastHash, data, hash):
        self.timestamp = timestamp
        self.lastHash = lastHash
        self.data = data
        self.hash = hash

    @staticmethod
    def genesis():
        return Block(**GENESIS_DATA)

    @staticmethod
    def mineBlock(self,lastHash, data):
        timestamp = time_ns()
        hash = cryptoHash(timestamp, lastHash, data)
        return Block(timestamp, lastHash, data, hash)

    @staticmethod
    def is_valid_block(lastBlock, block):
        if block.last_hash != lastBlock.hash:
            raise Exception('The block hash must equal the hash of last block')
        
        recHash = cryptoHash(block.timestamp, block.lastHash, block.data)
        if block.hash != recHash:
            raise Exception('The block hash is invalid')

    def to_json(self):
        return self.__dict__


    @staticmethod
    def from_json(block_json):
        return Block(**block_json)