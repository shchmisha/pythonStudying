from BlockChainNetwork.BlockChainNode.blockchain.block import Block
from BlockChainNetwork.BlockChainNode.blockchain.linkedList import LinkedList

class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]
        self.LLchain = LinkedList()
        self.length = 0

    def addBlock(self, data):
        block = Block.mineBlock(self.chain[-1].hash, data)
        self.chain.append(block)
        self.length+=1
        return block

    def addNewBlock(self, block):
        if(Block.is_valid_block(self.chain[-1], block)):
            tempChain = self.chain[:]
            tempChain.append(block)
            if Blockchain.isValidChain(tempChain):
                self.chain.append(block)
                self.length+=1
                return True
            else:
                print('block does not fit')
                return False
        else:
            print('corrupt block')
            return False

    # def addNewBlock(self, block):
    #     if(Block.is_valid_block(self.chain[-1], block)):
    #         self.chain.append(block)
    #         self.length+=1
    #         return True
    #     else:
    #         return False
    #
    # def addNewBlock(self, block):
    #     temp = self.chain[:]
    #     if (Blockchain.isValidChain(temp)):
    #         self.chain.append(block)
    #         return True
    #     else:
    #         print('corrupt block')
    #         return False

    def replaceChain(self, chain):
        if len(chain) <= len(self.chain):
            print("chain must be longer")
            return False

        if(not(Blockchain.isValidChain(chain))):
            print('chain not valid')
            return False
        print("valid chain")
        self.chain = chain
        self.length = len(chain)
        return True


    @staticmethod
    def isValidChain(chain):
        if chain[0].to_json() != Block.genesis().to_json():
            print('first block must be genesis')
            return False

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            if(not(Block.is_valid_block(last_block, block))):
                print('block '+str(i)+'is not valid')
                return False

        return True

    def to_json(self):
        return [block.to_json() for block in self.chain]

    @staticmethod
    def from_json(jsonChain):
        return [Block.from_json(blockData) for blockData in jsonChain]