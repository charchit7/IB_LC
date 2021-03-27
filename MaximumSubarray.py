"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum 
and return its sum.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


#kadane's Algorithm
# import sys
def maxSubArray(nums):#: list[int]) -> int:
    max_current = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global

print(maxSubArray([5,-3,5,5,-3,5]))