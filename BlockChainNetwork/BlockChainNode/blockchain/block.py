from time import time
from BlockChainNetwork.BlockChainNode.util.cryptoHash import cryptoHash
from BlockChainNetwork.BlockChainNode.util.config import GENESIS_DATA

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
    def mineBlock(lastHash, data):
        timestamp = time()
        hash = cryptoHash(timestamp, lastHash, data)
        return Block(timestamp, lastHash, data, hash)

    @staticmethod
    def is_valid_block(lastBlock, block):
        if block.lastHash != lastBlock.hash:
            return False

        recHash = cryptoHash(block.timestamp, block.lastHash, block.data)
        if block.hash != recHash:
            return False

        return True

    def to_json(self):
        return self.__dict__


    @staticmethod
    def from_json(block_json):
        return Block(**block_json)