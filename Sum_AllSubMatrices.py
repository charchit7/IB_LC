A = [ [1,2,3],
    [4,5,6],
    [7,8,9] ]

def submt(arr):
    n = len(arr)
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            #common among submatrix
            print((i+1),(j+1),(n-i),(n-j))
            common = (i+1)*(j+1)*(n-i)*(n-j)
            sum += arr[i][j]*common
    return sum

print(submt(A)) 