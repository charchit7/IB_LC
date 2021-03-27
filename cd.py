# def subsets(my_set,num):
#         result = [[]]
#         for x in my_set:
#             result = result + [y + [x] for y in result]
#         ans = -1
#         m = -1
#         for i in result:
#             if not sum(i)%num==0:
#                 m = len(i)
#                 ans = max(m,ans)
#         return ans

from itertools import permutations
a = int(input())
for i in range(a):
    x = int(input())
    arr = list(map(int,input().split(' ')))
    res = 0
    temp = 0
    for i in range(2,x+1):
        for i in list(permutations(arr,i)):
            for num in range(1,len(i)):
                res = i[num-1] - i[num] 
