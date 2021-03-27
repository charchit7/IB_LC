def short(arr):
    res = ""
    pointer1 = 0
    pointer2 = 1
    n = len(arr) 
    while pointer2<n-1:
        res += arr[pointer1]
        pointer1 += 2
        pointer2 += 2
    res += arr[n-2:n]
    return res


a = int(input())
for i in range(a):
    b = str(input())
    print(short(b))


# def even_array(arr):
#     even = 0
#     odd = 0
#     for i in range(len(arr)):
#         if arr[i] % 2 != i % 2:
#             if i % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
#     if even != odd:
#         return -1
#     else:
#         return even

# a = input()
# for i in range(int(a)):
#     x = int(input())
#     arr  = list(map(int,input().split()))
#     print(even_array(arr))
