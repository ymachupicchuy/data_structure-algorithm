Time Complexity
counFrequency = O(n)
buildHuffmannTree = > O(n log n)
huffmann_encoding_helper => O(n)
huffmann_encoding => O(n)
huffmann_decoding => O(n)
Python Priority Queue insert, get => (log n), qsize => O(n)

Overall => O(nlogn)

Space Complexity
O(n)

Explanation:
For the Huffmann Coding I used the Priority Queue, Recursion, Dictionary and LinkedList.
Getting and putting data into Priority Queue is O(log n).
Recursion used in the huffmann_encoding_helper to generate the codes. 
The builtin sorted function is used for in the buildHuffmannTree therefore the time overall time complexity is O(nlogn)



