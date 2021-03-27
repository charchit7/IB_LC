import math
def mins(arr):
    temp = arr[0]
    distance = 0
    math.floor
    for i in range(1,len(arr)):
        distance += math.floor(math.sqrt(pow((arr[i][0] - temp[0]),2) + pow((arr[i][1] - temp[1]),2)))
        temp = arr[i]
    return distance

print(mins([(0, 0), (1, 1), (1, 2)]))

A = [ (-7,1), (-13,-5) ]
print(mins(A))
ans1 = 6    

# A : [ 4, 8, -7, -5, -13, 9, -7, 8 ]
# B : [ 4, -15, -10, -3, -13, 12, 8, -8 ]

# ans = 108

# Note that because the order of covering the points is already defined, the problem just reduces to figuring out the way to calculate the distance between 2 points (A, B) and (C, D).

# Note that what only matters is X = abs(A-C) and Y = abs(B-D).

# While X and Y are positive, you will move along the diagonal and X and Y would both reduce by 1.
# When one of them becomes 0, you would move so that in each step the remaining number reduces by 1.

# In other words, the total number of steps would correspond to max(X, Y).