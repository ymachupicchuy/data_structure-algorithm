Time Complexity
loop range(len(sorted_list)) => O(n)
counting sort = > O(n)


Overall => O(n)

Space Complexity
O(k)

Explanation:
Before I rearrange the list I am sorting the list with counting sort which has a time complexity of O(n+k).
In the next step I differ between odd and even numbers and assign it to my variables resA and resB and return it

