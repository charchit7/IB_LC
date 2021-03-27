import math
def ans(x,y,n):
    for k in range(n,-1,-1):
        if k % x == y:
            return k

# run = int(input())
# for i in range(run):
#     x,y,n = map(int,input().split(' '))
#     print(ans(x,y,n))

def cc(n):
    if n == 1:
        return 0
    if n == 2:
        return -1
    count = 0
    temp = n
    while temp>=0:
        if temp%6==0:
            temp//6
            count +=1
            if temp == 1:
                return count
        else:
            temp//2
            if temp == 1:
                return count
    return count

run = int(input())
for i in range(run):
    x = int(input())
    print(cc(x))

