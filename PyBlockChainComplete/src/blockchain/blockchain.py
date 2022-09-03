from src.blockchain.block import Block

class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]

    def addBlock(self, data):
        block = Block.mineBlock(self.chain[-1], data)
        self.chain.append(block)
        return block

    def replaceChain(self, chain):
        if len(chain) <= len(self.chain):
            raise Exception('The incoming chain must be longer than the current chain')
        
        try:
            Blockchain.isValidChain(chain)
        except Exception as e:
            raise Exception(f'The incoming chain is invalid: {e}')

        self.chain = chain
    
    @staticmethod
    def isValidChain(chain):
        if chain[0] != Block.genesis():
            raise Exception('genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)

    def to_json(self):
        return [block.to_json() for block in self.chain]
    
    @staticmethod
    def from_json(jsonChain):
        return [Block.from_json(blockData) for blockData in jsonChain]