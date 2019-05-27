def sqrt(x):
    left, right = 0, x

    while left <= right:
        mid = (right + left)//2
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid

        if mid*mid > x:
            right = mid-1
        else:
            left = mid+1
    return None


'''
TEST
'''

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

def sqrt_shorter(x):
    if x > 0:
        return int(x**0.5)
    else:
        return None

def test1(num):
    if num is None or sqrt(num) == None:
        return False
    return sqrt(num) == sqrt_shorter(num)

print(test1(9))
# True
print(test1(-1))
# False
print(test1(None))
# False






