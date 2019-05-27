Time Complexity
append = > O(n)
size = > O(n)
isInList = > O(n)
union = > O(n)
intersection = > O(n)


Overall => O(n)

Space Complexity
O(n)

Explanation:
For the functions union and intersection I used LinkedList, Hash Set to eliminate first the duplicates and keep the values from the linked llist_1 in the memory. With a dictionary I would have duplicates. In the second step I am checking if the value are in the memory or not. This approach is used for union and intersection of Linkedlist. For the union function I am checking if the values from the second list is not in the first list and for intersection I am checking if the second list is in the first list.




