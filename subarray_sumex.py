def subarr(arr,number):
    n = len(arr)
    if sum(arr) % number !=0:
        return len(arr)
    else:
        i = 0
        while i < n and arr[i] % number == 0:
            i += 1
        j = n
        while j > 0 and arr[j-1] % number == 0:
            j -= 1
        if j-i <= 0:
            return -1
        else:
            return max(j-1,n-i-1)

print(subarr([0,1,0,1,0,1,0,1],2))
