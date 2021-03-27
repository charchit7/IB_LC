#INPUT-
# [
#     [1, 2],
#     [3, 4]
#  ]
#OUTPUT-
#  [
#     [3, 1],
#     [4, 2]
#  ]

a= [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
]
def rotate(A):
    n = len(A)
    for i in range(n):
        print('in outer i loop')
        for j in range(i+1,n):
            print('in outer j loop')
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(n//2):
        print('in i loop')
        for j in range(n):
            print('in j loop')
            # tmp = A[j][n-i-1]
            # print('in j loop')
            A[j][n-i-1], A[j][i] = A[j][i], A[j][n-i-1]
    return A

print(rotate(a))


##rotates the matrix in 90*
def mat(matrix):    
    n = len(matrix[0]) 

    
    for i in range(n//2+ n%2 ):
        for j in range(n-1-i*2):
            
            tmp = matrix[i][i+j]
            matrix[i][i+j] = matrix[n-1-i-j][i]
            matrix[n-1-i-j][i]= matrix[n-1-i][n-1-i-j]
            matrix[n-1-i][n-1-i-j]= matrix[i+j][n-1-i]
            matrix[i+j][n-1-i]=tmp
    return matrix
##################################################
##################################################

def short_m(matrix):
    matrix.reverse()
    
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def pythonicway(arr):
    #arr[::-1] flip matrix upside down, zip to transpose it.
    arr[:] = map(list, zip(*arr[::-1]))

