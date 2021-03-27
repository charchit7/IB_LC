# Given an array of integers A and multiple values in B which represents the indices of the array A around 
# which left rotation of the array A needs to be performed. Find the rotated array 
# for each value and return the result in the from of a matrix where  i'th row represents 
# the rotated array for the i'th value in B.

# Input 1:
#     A = [1, 2, 3, 4, 5]
#     B = [2, 3]

# Output 1:
#     [ [3, 4, 5, 1, 2]
#       [4, 5, 1, 2, 3] ]

# A = [ 6, 31, 33, 13, 82, 66, 9, 12, 69, 21, 17, 2, 50, 69, 90, 71, 31, 1, 13, 70, 94, 46, 89, 13, 55, 54, 67, 97, 28, 27, 62, 34, 41, 18, 15, 35, 13, 84, 93, 27, 89, 23, 6, 56, 94, 40, 54, 95, 47 ]
# B = [ 88, 85, 98, 36, 66, 40, 30, 26, 51, 77, 62, 60, 92, 64, 53, 86, 24, 53, 85, 49, 57, 29, 32, 60, 75, 82, 17, 23, 67, 51, 23, 11, 70, 59 ]
A = [1, 2, 3, 4, 5]
B = [2, 3]

def MRA(A,B):
    ans = []
    for i in B:
        ans.append(A[i%len(A):]+ A[:i%len(A)])
    return ans
print(MRA(A,B))
