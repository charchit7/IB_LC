#asked in Google #leetcode jump Game 2 
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        swaps = 0
        for i in range(n):
            print('in for loop',i)
            while A[i] != i:
                print('in while', A[i])
                idx = A[i]                   
                tmp = A[idx]
                A[idx] = A[i]
                A[i] = tmp
                print('arra',A)
                swaps += 1
                
        return swaps
A = [1, 2, 3, 4, 0]
B = [2, 0, 1, 3]
a = Solution()
# print(a.solve(B))


#mark the ith index as visited in the visited_arr and then go to j = A[j].second that is the second value corresponding
#to the ith index of the value at that index. So, mark that element at that index visited.   So, while we are at the 
# corresponding value at that index we check that index too, that is what we visited check its previous location too.
# mark that as visited too as well. IF that is visited break out of our cycle. 
# Also, on every iterattion of updating the J we will increament the cycle count +1. Final Ans - Cycle_Size -1..

def min_swap(A):
    swaps = 0
    for i in range(len(A)):
        while A[i] != i:
            temp = A[i]
            A[i] = A[temp] 
            A[temp] = temp
            swaps += 1
    return swaps
print(min_swap(A))