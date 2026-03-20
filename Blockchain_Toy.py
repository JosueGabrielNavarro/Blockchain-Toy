import json
import hashlib

# We need a class that fabricates the blocks in the blockchain
class Block:
    def __init__(self, index: int, content: str, prev_hash: str):
        self.index = index
        self.content = content
        self.prev_hash = prev_hash

        self.hash = self.calculateHash ()
    
    # Our hash calculator using SHA 256
    def calculateHash(self) -> str:
        dataBlck = {
            'index': self.index,
            'content': self.content,
            'prev_hash': self.prev_hash
        }

        # Convert into text
        textBlck = json.dumps(dataBlck, sort_keys=True)

        # Return the hash
        return hashlib.sha256(textBlck.encode('utf-8')).hexdigest()
    
# We need our blockchain class that actually conects the block
class Blockchain:
    def __init__(self):
        self.chain = [] # The list will contain our blocks

        # The list will initiate the genesis block
        self.chain.append(self.genesisBlck())
        
    # The function creates the genesis block
    def genesisBlck(self) -> Block:
        return Block(0, '000000000000000000000000', '00000000000000000000000000000000000000')
    

    # The function gets the last block in the chain
    def getLastBlck(self) -> Block:
        lastBlck = self.chain[-1]
        return lastBlck
    
    # The function we will use to add new block to the chain
    def addBlck(self, add: Block):
        lastBlck = self.getLastBlck()
        add.prev_hash = lastBlck.hash
        add.hash = add.calculateHash()
        self.chain.append(add)
    
    # Our detector if a change ocurred
    def ischainValid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.calculateHash() != current_block.hash:
                return False
            if current_block.prev_hash != previous_block.hash:
                return False
        return True

if __name__ == "__main__":
    try:
        # We start Blockchain
        myCoin = Blockchain()

        myCoin.addBlck(Block(1, 'Satoshi sent 50 BTC to Hal Finney', ''))
        myCoin.addBlck(Block(2, 'Hal Finney sent 20 BTC to Gabriel', ''))
        myCoin.addBlck(Block(3, 'Gabriel sent 5 BTC to Vitalik', ''))

        myCoin.chain[1].content = 'Hal Finney sent 5000 BTC to Hacker'
        myCoin.chain[1].hash = myCoin.chain[1].calculateHash()
        print(f'Is the Chain Valid? {myCoin.ischainValid()}')



        # We use a Loop to get the information of our chain
        for blck in myCoin.chain:
            print(f'index: {blck.index} | hash: {blck.hash[:10]} | prev_hash: {blck.prev_hash[:10]}')
    except Exception as e:
        print(f'System Error: {e}')