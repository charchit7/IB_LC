def square(num):
    x = num
    while x * x > num:
        x = (x + num // x) // 2
        print(x)
    return x * x == num
#Newtons method to find the square root
#we can also use the binary search also to get the desired optput.

print(square(5))

#shortest method
# return int(x**0.5)


import math
val = 8


def s1quare(num):
    low = 1
    high = num
    while low <= high:
        mid = low + (high - low)//2
        if mid == num//mid: # check on num//mid
            return mid
        elif mid < num//mid:
            low = mid+1
        else:
            high = mid - 1
    return high

assert s1quare(val) == math.floor(math.sqrt(val))
print(s1quare(val))

