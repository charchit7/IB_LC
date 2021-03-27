# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
a=[[1,4],[4,5],[8,10]]
b = [[1,3],[2,6],[8,10],[15,18]]

def merge(arr):
    res = []
    for i in sorted(arr, key= lambda x : x[0]):
        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], i[1])
        else:
            res.append(i)
    return res

# print(merger(a))
print(merge(a))
print(merge(b))