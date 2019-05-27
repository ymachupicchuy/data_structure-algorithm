# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, path, info):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(path)

    def insert(self, path, info):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        last = path[-1]
        for key in path:
            if last == key:
                node.children[key] = RouteTrieNode(info)
            else:
                node.children[key] = RouteTrieNode('not found handler')

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
        node = self.root
        if path[0] == '/':
            return node.data
        
        for key in path:
            if key not in node.children:
                return 'not found handler'
        node = node.children[key]
        return node.data
          
          
class RouteTrieNode:
    def __init__(self, data):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.data = data

    def insert(self, data):
        ## Add a child node in this Trie
        node = RouteTrieNode(data)
        self.children[data] = node

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, data, info):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(data, info)

    def add_handler(self, path, info):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pathList = self.split_path(path)
        _path = [x for x in pathList if x]
        self.root.insert(_path, info)

    
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if len(path) == 1:
             _path = path
        else:
            pathList = self.split_path(path)
            _path = [x for x in pathList if x]
        return self.root.find(_path)
       
    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')


'''
TEST
'''
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))


router = Router("root handler", "not found handler")
router.add_handler("/home/me", "me handler")  
print(router.lookup("/"))  
# router handler
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/about")) 
# not found handler
print(router.lookup("/home/about/"))
# not found handler
print(router.lookup("/home/about/me"))
# not found handler


router = Router("root handler", "not found handler")
router.add_handler("/home/me", "me handler")
print(router.lookup("/"))
# router handler
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/me"))
# me handler
print(router.lookup("/home/me/"))
# me handler
print(router.lookup("/home/next/me"))
# not found handler


router = Router("root handler", "not found handler")
router.add_handler("/-", "- handler")
print(router.lookup("/"))
# router handler
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/-"))
# not found handler
print(router.lookup("/-/"))
# - handler
print(router.lookup("/home/next/me"))
# not found handler
