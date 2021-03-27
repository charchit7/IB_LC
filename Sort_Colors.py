"""
Given an array sort it in place so that same colors are adjacent and in order - red, white, blue
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow Up- Can you do in 1 pass algorithm
"""
#can do with counting sort - 2 pass algorithm

arr  = [ 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 2, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 0, 1, 1, 0, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2 ]
def sort_color(arr):
    count = [0 for i in range(max(arr)+1)]
    for i in arr:
        count[i] += 1
    #accumulate , this means that the array now countains i element at c[i]
    for i in range(1,max(arr)+1):
        count[i] =  count[i-1] + count[i] 
    
    res = [0 for i in range(len(arr))]
    for val in arr:
        index = count[val] - 1
        res[index] = val
        count[val] -= 1
    return res
# print(sort_color(arr))


#one pass algorithm
def sort_c(arr):
    red = 0
    white = 0
    blue = 0
    for i in arr:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        else:
            blue += 1
    print(red,white,blue)
    for i in range(red):
        arr[i] = 0
    for i in range(red, red+white):
        arr[i] = 1
    for i in range(red+white, blue+red+white):
        arr[i] = 2
    return arr

# print(sort_c(arr))

#dutch national flag problem:
def sc(nums):
    red, white, blue = 0, 0, len(nums)-1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
    return arr

print(sc(arr))