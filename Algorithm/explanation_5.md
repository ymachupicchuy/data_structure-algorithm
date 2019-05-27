Time Complexity
insert, find = > O(n)
suffixes => O(n2)

Overall => O(n2)

Space Complexity
O(n)

Explanation:
For the autocompleter task I am using children dictionary to insert and find the a word.

insert function: 
    If a char not exist then I am adding the node in the children dictionary of an node. If I reach the end then I mark the node is_word to True which will be relevant for finding a word.

find function:
    If a char not exist in my trie then I am returning False. Otherwise I am returning the node


suffix function:
    Here I am interating the trie and using the char and node in my substree and extend my suffix +  i.
    Here I had my problems to understand yield and recursion works. I need to spent more time on it but it would be great to see different appraochs (iterative, recursion, without yield) to understand it better.
