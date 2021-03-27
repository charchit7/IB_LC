def check(arr):
    count =0
    temp = sorted(arr)
    for i in range(len(arr)):
        if temp[i] != arr[i]:
            count +=1
    return count//2

a = int(input())
for i in range(a):
    x = int(input())
    arr = list(map(int,list(input().split())))
    print(check(arr))