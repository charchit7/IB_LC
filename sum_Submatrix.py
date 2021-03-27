A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
 
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]


# A = [   [5, 17, 100, 11],
#     [0, 0,  2,   8]    ]
# B = [1, 1]
# C = [1, 4]
# D = [2, 2]
# E = [2, 4]

def m(arr,a,b):
    sum = 0
    # height
    for i in range(a[0],b[0]+1):
        #width
        for j in range(a[1],b[1]+1):
           sum += arr[i-1][j-1]
    return sum



def sumMatrix(arr,b,c,d,e):
    top = list(zip(B,C))
    bottom = list(zip(D,E))
    
    for i in range(len(top)):
        print(m(arr,top[i],bottom[i]))

# print(sumMatrix(A,B,C,D,E))


#################################### OPTIMIZED METHOD ###################
def row_prefix(arr):
    for i in arr:
        for j in range(1,len(arr)):
            i[j] = i[j-1] + i[j]
    return arr

def column_prefix(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1,n):
            arr[j][i] = arr[j][i] + arr[j-1][i]
    return arr

def subSum(A,B,C,D,E):
    sum = 0
    row_prefix(A)
    print(A)
    column_prefix(A)
    print(A)
    for i in range(len(B)):
        x1 = B[i]
        y1 = C[i]
        x2 = D[i]
        y2 = E[i]
        print(A[x2-1][y2-1])
        print(A[x2-1][y1-2])
        print(A[x1-2][y2-1])
        print(A[x1-2][y1-2])
        print('################')
        # sum += A[x2-1][y2-1] - A[x2-1][y1-2] - A[x1-2][y2-1] + A[x1-2][y1-2]
        print(sum)

print(subSum(A,B,C,D,E))
# Sum between (x1, y1) and (x2, y2) is,
# arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]

# [[1, 3, 6], 
#  [4, 9, 15], 
#  [7, 15, 24]]

#  [1,3,6]
#  [5,12,21]
#  [12,27,45]

1,1) (2,2) 
# B = [1, 2]
# C = [1, 2]
# D = [2, 3]
# E = [2, 3]
A[1][-1]