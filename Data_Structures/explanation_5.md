Time Complexity
createGenesisBlock = > O(1)
getLatestBlock = > O(1)
addBlock = > O(1)
isValid = > O(n)

Overall => O(n)

Space Complexity
O(n)

Explanation:
The blockchain application uses a LinkedList and a chain (Stack). Adding a block and connecting it with the latestBlock and adding it to the chain is doing the most work. I have created a isValid function to validate the blockchain (previous.hash != currentBlock.calc_hash()) and it is also used for testing purposes to check if the blockchain is valid or not.



