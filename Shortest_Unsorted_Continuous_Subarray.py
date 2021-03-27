# given an array you need to find continous smallest subarray such that if you sort this array in ascending order
# the whole array will be sorted.

# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
arr = [1,2,3,4]
#my method 0(n), 0(n)
def practice(arr):
    #create a temp array which is sorted to compare with previous array for val each val at that index
    temp = sorted(arr)

    #counter to measure wrong value index
    counter_start = 0
    counter_stop = 0
    
    #loop for first value which missmatches
    for i in range(len(arr)):
        if arr[i]!= temp[i]:
            counter_start = i
            break
    
    #loop for mismatch fist value from the last index
    for j in range(-1,-len(arr)-1,-1):
        if arr[j]!=temp[j]:
            counter_stop = j
            break

    #if counter_stop is 0 that means array is sorted. eg, 1,2,3,4, this should return 0 insted of 1 for our case.
    if counter_stop>0:
        return len(arr[counter_start:counter_stop+1])
    else:
        return '0'

# print(practice(arr))
    

#use the idea of selection sort    
def try_out(arr):
    #mark counter's to track the location of the unsorted path
    start_counter = len(arr)
    close_counter = 0

    #start from initial value, go till second last to compare value
    for i in range(len(arr)-1):
        #compare with each value
        for j in range(i,len(arr)):
            #if the i'th value is greater that means the array is not sorted.
            if arr[i] > arr[j]:
                #we take min and max value to get the result as start to stop list.
                start_counter = min(start_counter,i)
                close_counter = max(close_counter,j)
    #this indicates that the list is sorted or not if < then sorted
    if close_counter-start_counter < 0:
        return '0'
    else:
        print(close_counter,start_counter)
        return arr[start_counter:close_counter+1]

print(try_out(arr))


#use the sorted arr
def method_3(arr):
    sorted_arr = sorted(arr)
    start = len(arr)
    end = 0
    for i in range(len(arr)):
        if sorted_arr[i] != arr[i]:
            start = min(start, i)
            end = max(end, i)
    if end- start < 0:
        return 0
    else:
        return arr[start:end+1]
print(method_3(arr))


#using stack
def method_4(arr):
    stack = []
    l = len(arr)
    r = 0
    for i in range(len(arr)):
        while (len(stack)!=0 and arr[stack[-1]] > arr[i]):
            l = min(l , stack.pop())
        stack.append(i)
    stack.clear()
    for i in range(len(arr)-1,-1):
        while len(stack) != 0 and arr[stack[-1]] < arr[i]:
            r = max(r, stack.pop())
        stack.append(i)
    if r-l > 0:
        return 0
    else:
        return arr[l:r+1]
print(method_4(arr))

def method_5(arr):
    min1 = 100000
    max1 = -100000
    for i in range(1,len(arr)-1):
        if arr[i] < arr[i - 1]:
            min1 = min(min1, arr[i])
        else:
            break
    for i in range(len(arr)-2,-1):
        if arr[i] > arr[i+1]:
            max1 = max(max1, arr[i])
        else:
            break

    left = 1000000
    right = -100000
    for i in range(len(arr)):
        if min1 < arr[i]:
            left = i
            break   
    for j in range(len(arr)-1 , -1):
         if  max1 > arr[j]:
             right = j
             break
    
    
    print(left, right)
    if right - left < 0:
        return 0
    else:
        return arr[right:left+1]

print(method_5(arr))


#O(n3)
"""
import sys
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                min1 = sys.maxsize
                max1 = -1
                prev = -1
                for k in range(i,j):
                    min1 = min(min1, nums[k])
                    max1 = max(max1, nums[k])
                if ((i > 0 and nums[i - 1] > min1) or (j < len(nums) and nums[j] < max1)):
                    continue
                k = 0
                while (k < i and prev <= nums[k]):
                    prev = nums[k]
                    k += 1
                if (k != i):
                    continue
                k = j
                while (k < len(nums) and prev <= nums[k]):
                    prev = nums[k]
                    k += 1
                if (k == len(nums)):
                    res = min(res, j - i)
        return res

"""

    