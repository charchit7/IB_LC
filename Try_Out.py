A = [   [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]   ]

n = len(A)
arr=[[0]*(n+1) for i in range(n+1)]
print(arr)
#columwise sum
for i in range(1, n, 1): 
    for j in range(0, n, 1): 
        arr[i+1][j+1] = A[i][j] + arr[i][j+1]
print(arr)
        