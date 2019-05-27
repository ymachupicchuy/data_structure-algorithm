Time Complexity
insert, findm, lookup, split_path = > O(n)

Overall => O(n)

Space Complexity
O(n)

Explanation:
For the autocompleter task I am using children dictionary to insert and find the a word.

insert function: 
    For inserting a node I am comparing the last value of the path and current key which means I am in the end of my list and adding the RouterTrieNode with its info such as "root handler" or "about handler" otherwise I am adding a node with "not found hanlder" as info. An handler such as "is_leaf" could be also used instead of this approach.

find function:
   Checking if the word exist in my trie. If not I am return "not found handler". After the loop reach the end I am collect the last node and return the node.data which includes if is a root handler or about handler or something else.
