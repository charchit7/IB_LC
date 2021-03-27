def can_Jump(A):
    n = len(A)-1
    for i in range(n-1,-1,-1):
        if i+ A[i] >= n:
            # print('checking',i,A[i])
            n = i
    if n == 0:
        return True
    return False

A = [3,2,1,1,4] 
print(can_Jump(A))


nums = [2,3,1,1,4]
def jump_array(arr):
    #counter to see the path we have covered
    reach = 0
    #looping 
    for index, value in enumerate(arr):
        #if reach is smaller than the index that means that we can't move forward
        if reach < index:
            return False
        # here we are taking value + index to denote that we are moving forward
        reach = max(reach, index + value)
    return True


nums = [2,3,1,1,4]


#in reverse order 
def jump_game_rev(arr):
    goal = len(arr)-1
    for i in range(len(arr)[::-1]):
        #checking if the value including the index is greater than the goal then we update the 
        #goal that we are reaching.
        if i + arr[i] >= goal:
            goal = i
    return not goal