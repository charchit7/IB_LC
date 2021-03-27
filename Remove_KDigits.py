# Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

def practice(string, nu):
    #base case if the number of elements we wan't to remove is 
    #equal to the number of elements we have 

    n = len(string)
    if nu == n:
        return "0"
    
    #create a stack to store the value for evaluation
    stack = []
    #check for the last element of the stack if the element at the last 
    #is greater than the current element we remove that element.

    for i in string:
        while nu and stack and (int(stack[-1]) > int(i)):
            stack.pop()
            nu -= 1
        stack.append(i)

    #this code is important, this executes when there is no greater element 
    #in the stack that means the greater element is at the end of the list
    #so we need to remove that to satisfy the condition of K.
    #to test this case take condition str = "112" k = 1
    while nu >0:
        stack.pop()
        nu -= 1
    
    return "".join(stack).lstrip('0') or "0"


#alternate sol    def removeKdigits(self, num: str, k: int) -> str:
def tester(string, k):
    stack=[]
    m=k
    for curr in num:
        while m and stack and stack[-1]>curr:
            stack.pop()
            m-=1
        stack.append(curr)
    ans= ''.join(stack[0:len(num)-k]).lstrip("0")
    if len(ans)!=0:
        return ans
    else:
        return "0"