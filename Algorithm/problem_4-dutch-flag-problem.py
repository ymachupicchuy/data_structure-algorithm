
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    return sortArr(input_list)

def sortArr(arr):

    low = -1
    mid = 0
    high = len(arr)

    while mid < high:
        if arr[mid] == 0:
            low += 1
            swap(arr, low, mid)
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            high -= 1
            swap(arr, mid, high)
    return arr

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


def test_sortArr(nums):
    return sortArr(nums) == [0, 1, 2]


print(test_sortArr([1, 2, 0]))
# True

print(test_sortArr([2]))
False

print(test_sortArr([]))
False

