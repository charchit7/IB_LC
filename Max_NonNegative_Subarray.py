#asked in Google interview

# def MNNS(arr):
#     current_sum = 0
#     max = 0
#     curren_range_x = 0
#     current_range_y =0
#     max_range_x = 0
#     max_range_y = 0

#     for i in range(len(arr)):
#         if arr[i] > 0:
#             current_sum += arr[i]
#             current_range_y += 1

#             if current_sum > max:
#                 max = current_sum
#                 max_range_x = curren_range_x
#                 max_range_y = current_range_y
#             else:
#                 continue
#         else:
#             current_sum = 0
#             curren_range_x = i + 1
#             current_range_y= i + 1
#     return max_range_x, max_range_y, curren_range_x, current_range_y
# A = [1, 1, 1, -7, 2, 3]
# print(MNNS(A))

A = [0,0,-1,0]
B = [1, 2, 5, -7, 2, 3]
C = [10, -1, 2, 3, -4, 100]
from itertools import groupby


def answer(arr):
    answer = -float('inf')
    res = []
    temp = groupby(arr, key = lambda x: x >= 0)
    for key, val in temp:
        if key == True:
            a = list(val) 
            # why I am taking a here is because since group by are iterators it gets vanished after 1 use
            # so if we use list(val) again without initializing to any var it will be vanished no result will be there.
            if sum(a) > answer:
                answer = sum(a)
                res = a
    return res
 
print(answer(A))
print(answer(B))
print(answer(C))