def rightRotate (a, n, op, c): 
    t = a[c] 
    for i in range(c, op, -1):
        a[i] = a[i - 1] 
    a[op] = t 

def rearrange(a, n): 
    op = -1
    for ind in range(0, n): 
        if op >= 0: 
            if ( (a[ind] >= 0 and a[op] < 0) or (a[ind] < 0 and a[op] >= 0)):  
                print(a,op)
                rightRotate(a, n, op, ind)
                print('after',a,ind)
                 
                if (ind - op > 2):
                    print('in if ind-op')
                    op = op + 2 
                else:
                    print('in rlse')
                    op = -1
        if (op == -1):  
            if ((a[ind] >= 0 and (ind & 1) == 0) or (a[ind] < 0 and (ind & 1) == 1)): 
                op = ind 
                
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A): 
       rearrange(A, len(A))
       return A

a = [1,-2,-3,-4,5]      
b = Solution()
print(b.solve(a)) 
