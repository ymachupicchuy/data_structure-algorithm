import hashlib, time
class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
  
    def createGenesisBlock(self):
        ts = time.time()
        return Block(ts, 'Genesis block', '0')

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previous_hash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calc_hash()
        self.chain.append(newBlock)

    # Test Function
    def isValid(self):
        if len(self.chain) == 0:
            return False
        for i in range(len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]
        
        if currentBlock.hash != currentBlock.calc_hash():
            return False

        if currentBlock.previous_hash != previousBlock.hash:
            return False

        return True
        

'''
TEST
'''
blockchain = Blockchain()


def test1():
    ts = time.time()
    blockchain.addBlock(Block(ts, 'Mango'))
    blockchain.addBlock(Block(ts, 'Papaya'))
    blockchain.addBlock(Block(ts, 'Banana'))
    return blockchain.isValid()

print(test1() == True)
#True

def test2():
    ts = time.time()
    for x in range(1000):
        blockchain.addBlock(Block(ts, 'Melone'))
    return len(blockchain.chain)

print(test2() == 1004)
# True

def test3():
    ts = time.time()
    del blockchain.chain[:]
    return blockchain.isValid()

print(test3())
# False

  










