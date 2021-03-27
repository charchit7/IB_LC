# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.


"""
METHOD 1
def rain_trap(arr):

    for i in range(1,len(arr)-1):
        
        #this loop will give the max value till i'th index
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        
        #this loop will give the max value from right to left till the index i
        right = arr[i]
        for k in range(i+1,len(arr)):
            right = max(right, arr[k])

        #calculate the accumulated val and store it
        res = 0
        res = res + min(left,right) - arr[i]

"""

"""
#METHOD 2
a = [3,0,2,0,4]
def rain_trapped(arr):
    #creating an array which will store the max of left everytime we traverse from left to right.
    left_high = [0]*len(arr)
    #creating an array which will store the max of right evertime we traverse from right to left.
    right_high = [0]*len(arr)

    left_high[0] = arr[0]
    for i in range(1,len(arr)):
        left_high[i] = max(left_high[i-1], arr[i])
    
    right_high[-1] = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        right_high[i] = max(right_high[i+1], arr[i])
    
    #calculating the accumutated amount in the var res.
    #its like if we are at 0 index, then the array will store the min amount of val - value at that index.
    res = 0
    for i in range(len(arr)):
        res = res + (min(left_high[i],right_high[i]) - arr[i])
    
    return res

print(rain_trapped(a))



"""
"""def rain_trapped(arr):
    #instead of storing the max till that index in array we will deal with them as we go along.

    right_max = 0
    left_max = 0

    low = 0
    high = len(arr)-1

    res = 0

    while low <= high:
        #this condition is when fist element is smaller than last element, so we look from left to right.
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                res += left_max - arr[low]
            low += 1
        #this will work if the right element is bigger so we now movef from right to left.
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                res += right_max - arr[high]
            high -= 1
    return res

print(rain_trapped(a))"""