'''
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
'''
#we need to do in O log(n) and O(1) space complexity.
import collections
def Single_Element(arr):
    dictionary = collections.Counter(arr)
    for key,value in dictionary.items():
        if value == 1:
            return key

#O(1)Space and O(logn) Complexity
def SingleElement(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] == arr[mid ^ 1]:
            low = mid + 1
        else:
            high = mid 
    return arr[low]
        
print(SingleElement([1,1,2,3,3,4,4,8,8]))