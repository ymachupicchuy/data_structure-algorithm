def sqrt(x):
    left, right = 0, x

    while left <= right:
        mid = (right + left)//2
        if mid**2 <= x < (mid+1)**2:
            return mid

        if mid**2 > x:
            right = mid-1
        else:
            left = mid+1

def sqrt_shorter(x):
    return int(x**0.5)

'''
TEST
'''

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")


# Test shorter approach

# print("Pass" if (3 == sqrt_shorter(9)) else "Fail")
# print("Pass" if (0 == sqrt_shorter(0)) else "Fail")
# print("Pass" if (4 == sqrt_shorter(16)) else "Fail")
# print("Pass" if (1 == sqrt_shorter(1)) else "Fail")
# print("Pass" if (5 == sqrt_shorter(27)) else "Fail")



