## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        node = TrieNode()
        self.children[char] = node
    
    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        node = self.children

        if self.is_word:
            yield suffix

        for i, k in node.items():
            for x in k.suffixes(suffix + i):
                yield x

       
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True
            

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return node
    
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixNode = MyTrie.find('f')
if prefixNode:
    prefixNode.suffixes()
    print('\n'.join(prefixNode.suffixes()))
else:
    print(prefix + " not found")
