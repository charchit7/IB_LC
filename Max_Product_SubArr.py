# Given an integer array nums, 
# find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
import math
def max_product(arr):
    B = arr[::-1]
    for i in range(1,len(arr)):
        arr[i] *= arr[i - 1] or 1
        B[i] *= B[i - 1] or 1
    # return max(arr+B)
    max1 = -math.inf
    for i in range(len(arr)):
        max1 = max(max1, arr[i], B[i])
    
    return max1, arr, B
arr = [1,2,0,3,4]
print(max_product(arr))


def maxProduct1(nums):
    prefix, suffix, max_so_far = 0, 0, float('-inf')
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i]
        suffix = (suffix or 1) * nums[~i]
        max_so_far = max(max_so_far, prefix, suffix)
    return max_so_far


def maxProduct(self, A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(A + B)