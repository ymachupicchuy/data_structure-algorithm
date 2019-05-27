Time Complexity
find_files = > O(n2)
os.walk = > O(n)

Overall => O(n^2)

Space Complexity
O(n)

Explanation:
I have used nested loop and the os.walk to to find the folder which includes the given suffix.
os.walk is scanning all the directories and subtrees. Instead of using os.dir and os.path, etc.. I just used os.walk.



