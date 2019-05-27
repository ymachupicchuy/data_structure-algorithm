class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dic = dict()

        # initialize double LL
        self.head = DoubleNode(0, 0)
        self.tail = DoubleNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dic:
            n = self.dic[key]
            self.deleteNode(n)
            self.addNode(n)
            return n.value
        return -1
            
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.dic:
            self.deleteNode(self.dic[key])
        n = DoubleNode(key, value)
        self.addNode(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self.deleteNode(n)
            del self.dic[n.key]

    def addNode(self, node):
        self.tail.prev.next = node
        self.tail.prev = node
        node.prev = self.tail.prev
        node.next = self.tail


'''
TEST
'''
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)

def test1(val):
    return our_cache.get(val)
print(test1(1))
# returns 1

def test2(val):
    return our_cache.get(val)
print(test2(3))
# returns -1

def test3(val):
    return our_cache.get(val)
print(test3(None))   
# return -1




