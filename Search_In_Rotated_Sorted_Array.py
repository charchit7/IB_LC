# So, the problem is that given an array sorted in ascending order is rotated at some pivot, 
#by pivot we means that let's say we have array.
# a = [1,2,3,4,5], now this array is rotated in such a way that the first few elements are 
# shifted to the end so the array becomes. a = [3,4,5,1,2].

# So, here we can use binary search to get the result in O(logn).


def search(nums: [int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1
    low = 0
    high = n -1
    first = nums[0]
    while(low <= high):
        mid = low + (high - low) // 2  #this is used to not to have overflow.
        value = nums[mid]
        if value == target:
            return mid
        
        am_big = value >= first
        target_big = target >= first
        if am_big == target_big:
            if value < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if am_big:
                low =  mid + 1
            else:
                high = mid + 1

    return -1 
