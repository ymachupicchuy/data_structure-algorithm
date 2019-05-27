Time Complexity
qsort = > O(nlogn)


Overall => O(nlogn)

Space Complexity
O(n)

Explanation:
As before in problem_3 I am using Quicksort for sorting my unsorted array. The different between my Quicksort in problem_3 is in this example in ascend order qsort(left) + [pivot] + qsort(right).
This approach of Quicksort has a space complexity of O(n) and could be improved if I sort it in place. I decide to use this approach because it was easiert to apply for me :-) 

