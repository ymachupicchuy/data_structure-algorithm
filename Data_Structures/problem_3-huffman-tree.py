import sys
from queue import PriorityQueue
class Node:
    def __init__(self, value, priority, right=None, left=None):
        self.value = value
        self.priority = priority
        self.right = right
        self.left = left
    
    def __lt__(self, obj):
        return self.priority < obj.priority


def countFrequency(data):
    listFreq = dict()
    for char in data:
        if char in listFreq.keys():
            listFreq[char] += 1
        else:
            listFreq[char] = 1
    return listFreq


def buildHuffmannTree(text):
    pq = PriorityQueue()
    freq = countFrequency(text.replace(' ', ''))

    for key in sorted(freq, key=freq.get):
        pq.put(Node(key, freq[key]))
        
    while pq.qsize() > 1:         
        left = pq.get()
        right = pq.get()

        newSum = left.priority + right.priority
        pq.put(Node(None, newSum, left, right))
    return pq.get()  

def huffman_encoding_helper(root, current_code, codes, reversed_codes):
    if root == None:
        return

    if root.left == None and root.right == None:
        codes[root.value] = current_code
        reversed_codes[current_code] = root.value
    
    huffman_encoding_helper(root.left, current_code + '0', codes, reversed_codes)
    huffman_encoding_helper(root.right, current_code + '1', codes, reversed_codes)

def huffman_encoding(data, reversed_codes):
    if data is None:
        return None, None

    root = buildHuffmannTree(data)
    current_code = ""
    encoded_text = ""
    codes = {}
 
    huffman_encoding_helper(root, current_code, codes, reversed_codes)

    for char in data.replace(' ', ''):
        encoded_text += codes[char]
    return encoded_text, root

def huffman_decoding(data, tree):
    current_code = ""
    decoded_text = ""

    for code in data:
        current_code += code
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""
    return decoded_text
        
        
if __name__ == "__main__":
    reversed_codes = {}
  
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence, reversed_codes)
 
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


'''
TEST
'''
reversed_codes = {}
def test1(a_great_sentence):
     encoded_data, tree  = huffman_encoding(a_great_sentence, reversed_codes)
     return encoded_data == '001010011101011010111101010011000010011100010100011110'

print(test1('The bird is the word'))
# False

def test2(a_great_sentence):
     encoded_data, tree  = huffman_encoding(a_great_sentence, reversed_codes)
     return encoded_data == '001010011101011010111101010011000010011100010100011111'

print(test2('The bird is the word'))
# False

def test3(a_great_sentence):
     encoded_data, tree  = huffman_encoding(a_great_sentence, reversed_codes)
     return encoded_data == None

print(test3(None))
# True


