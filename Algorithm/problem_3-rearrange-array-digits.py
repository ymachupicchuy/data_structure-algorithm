def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    resA = 0
    resB = 0

    sorted_list = qsort(input_list)
    
    for i in range(len(sorted_list)):
        # even
        if i % 2 == 0:
            resA = int('%d%d' % (resA, sorted_list[i]))
        # odd
        else:
            resB = int('%d%d' % (resB, sorted_list[i]))
    
    return [resA, resB]
    

def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    rest = arr[1:]
    left, right = [], []

    for el in rest:
        if el < pivot:
            left.append(el)
        else:
            right.append(el) 

    return qsort(right) + [pivot] + qsort(left)
   
  
rearrange_digits([4, 6, 2, 5, 9, 8])


'''
TEST
'''

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

def test_qsort(nums):
    return qsort(nums) == [9,8,7]

print(test_qsort([9,7,8]))
# True

print(test_qsort([None]))
# False

print(test_qsort([]))
# False
