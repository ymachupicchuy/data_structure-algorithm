Time Complexity
get_min_max = > O(n)

Overall = > O(n)

Space Complexity
O(1)

Explanation:
Using two variable maxVal and minVal for assigning the min and max value.
Iterate through the ints and figuring out the min and max value within the loop.
In the end I am return the value.
An binary search would not work because the list is unsorted and it need to be sorted first where the 
time complexity is O(nlogn). This would be not a good choice.
