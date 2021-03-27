# array = {5, 1, 3, 4, 2}
# Sort the above array. 

# array = {1, 2, 3, 4, 5}
# Now swap adjacent elemets in pairs.

# swap(1, 2)
# swap(3, 4)

# Now, our array = {2, 1, 4, 3, 5}
# and voila!, the array is in the wave form. 


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        #ret = [0]*n
        for i in range(0, n, 2):
            if i + 1 < n:
                A[i], A[i+1] = A[i+1], A[i]
        return A