# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.

def Is_Monotonic(arr):
    inc = True
    dec = True
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            inc = False
        if A[i] < A[i+1]:
            dec = False
    return inc or dec