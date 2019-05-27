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

    sorted_list = counting_sort(input_list)

    for i in range(len(sorted_list)):
        # even
        if i % 2 == 0:
            resA = int('%d%d' % (resA, sorted_list[i]))
        # odd
        else:
            resB = int('%d%d' % (resB, sorted_list[i]))
    
    return [resA, resB]
    

def counting_sort(arr):
       
        if not len(arr):
            return None

        minVal = min(arr)
        maxVal = max(arr)+1
        count = [0] * maxVal
        j = 0

        for val in arr:
            count[val] += 1

        for i in range(minVal, maxVal):
            while count[i] > 0:
                arr[j] = i
                j += 1
                count[i] -= 1
        return arr[::-1]

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

def test_counting_sort(nums):
    return counting_sort(nums) == [9, 8, 7]

print(test_counting_sort([9,7,8]))
# True

print(test_counting_sort([2]))
# False

print(test_counting_sort([]))
# False
