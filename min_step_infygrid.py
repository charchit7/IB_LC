# Note that because the order of covering the points is already defined, the problem just reduces to 
# figuring out the way to calculate the distance between 2 points (A, B) and (C, D).

# Note that what only matters is X = abs(A-C) and Y = abs(B-D).

# While X and Y are positive, you will move along the diagonal and X and Y would both reduce by 1.
# When one of them becomes 0, you would move so that in each step the remaining number reduces by 1.

# In other words, the total number of steps would correspond to max(X, Y).
          A  B    C  D
Input : [(0, 0), (1, 1), (1, 2)]


def coverPoints(X, Y):
    ret = 0
    n = len(X)
    if n == 0:
        return ret
    curr = (X[0], Y[0])
    
    for i in range(1,n):
        stepsX = abs(curr[0] - X[i])
        stepsY = abs(curr[1] - Y[i])
        ret += max(stepsX, stepsY)
        curr = (X[i], Y[i])
    return ret
























