"""
Given an unsorted integer array A of size N.
Find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
"""
A = [1, 10, 5]
B = [2,99999999]
#  out = 5
# After sorting, the array becomes [1, 5, 10]
#  Maximum difference is (10 - 5) = 5.


def max_gap(arr):
    if len(arr) < 2:
        return 
    res = 0
    arr.sort()
    for i in range(len(arr)-1):
        res = max(res, abs(arr[i]-arr[i+1]))
    return res
# print(max_gap(A))


def maximumGap(arr) -> int:
    def get_digit(n,no_of_bit):
        if no_of_bit == 1:
            return n%10
        n = n//(10**(no_of_bit-1))
        return n %10

    def Counting_Sort(arr, pas):
        # count = [0 for i in range(max(arr)+1)]
        count = [0 for i in range(max(arr)+1)]
        for val in arr:
            asperbit = get_digit(val,pas)
            count[asperbit] += 1

        #accumulate
        for i in range(1,len(count)):
            count[i] = count[i-1] + count[i]

        #new array to store the sorted array
        res = [0 for i in range(len(arr))]
        # for i in arr:
        for i in reversed(arr):
            val = get_digit(i,pas)
            index = count[val] - 1
            res[index] = i
            count[val] -= 1
        return res
    #method Rad
    def Radix_Sort(arr):
        turn = len(str(max(arr))) + 1
        for i in range(1,turn):
            arr = Counting_Sort(arr,i)
        return arr    
    if len(arr) < 2:
        return 0
    res = 0
    new = Radix_Sort(arr)
    for i in range(len(new)-1):
        res = max(res, abs(new[i]-new[i+1]))
    return res

# print(maximumGap(B))
from collections import namedtuple
def mc(array):

    if len(array) == 1 or len(set(array)) == 1:
        return 0

    Bucket = namedtuple('Bucket', ['minimum','maximum']) 
    buckets = [Bucket(float('inf'), -float('inf'))]*(len(array))
    
    minimum = min(array) 
    maximum = max(array) 
    
    for number in array: 
        index = (number - minimum)*(len(array) - 1) // (maximum - minimum) 
        currentBucket = buckets[index] 
        buckets[index] = Bucket(min(number, currentBucket.minimum), max(number,currentBucket.maximum))
    cleanedBucket = list(filter(lambda x: x.minimum!=float('inf') or x.maximum!=-float('inf'), buckets))


    res = 0     
    for i in range(1,len(cleanedBucket)): 
        res = max(res, cleanedBucket[i].minimum - cleanedBucket[i-1].maximum) 
    return res

print(mc(A))
print(mc(B))
print(mc([10]))