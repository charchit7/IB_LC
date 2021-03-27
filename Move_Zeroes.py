#Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
a = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pointer = 0
    for i in nums:
        if i!=0:
            nums[pointer] = i
            pointer += 1
    for i in range(pointer, len(nums)):
        nums[i] = 0
        
    return nums

print(moveZeroes(a))