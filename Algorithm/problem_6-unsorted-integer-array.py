def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    maxVal = 0
    minVal = None

    for num in ints:
        if num > maxVal:
            maxVal = num
        
        if minVal == None:
            minVal = num
        else:
            if num < minVal:
                minVal = num
     
    return (minVal, maxVal)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
