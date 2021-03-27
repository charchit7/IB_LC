def chunk(arr):
    ans = ma = 0
    for i, x in enumerate(arr):
        print(i,x)
        ma = max(ma,x)
        print('ma max',ma)
        if ma == i:
            print('in condition',ma,i)
            ans += 1
    return ans

print(chunk([1,2,3,4,0,5,6,7]))