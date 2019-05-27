Time Complexity
loop range(len(sorted_list)) => O(n)
qsort = > O(nlogn)


Overall => O(nlogn)

Space Complexity
O(n)

Explanation:
Before I rearrange the list I am sorting the list and for that I am using Quicksort which has a time complexity of O(nlogn).
For Quicksort I am using left and right list and sort it in descend order qsort(right) + [pivot] + qsort(left) and merge it together.

In the next step I differ between odd and even numbers and assign it to my variables resA and resB which I return

