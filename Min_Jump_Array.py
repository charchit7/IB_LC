def jump(A):
    # destination is the last index
    destination = len(A) -1 
    covered_area = 0
    last_jump_index = 0
    number_of_jumps = 0

    #just in case if there are single element in array.
    if len(A) == 1:
        return 0
    
    #approach:-
    """
    We loop through elements in the array and update the covered
    area which is the maximum area covered when moving from one 
    index to next. let's say index 1 covers 3 area and index 2
    covers 2 area then the max is 3area cover. We are adding i+A[i]
    because it denotes we are moving in a direction.
    Now, if the index is the index we have covered, then update the
    last_jump_index and number_of_jumps since we have covered that 
    part and we need to move to the next index.
    If the covered are crosses the destination or is reached.
    Then return the value.
    """
    for i in range(len(A)):
        covered_area = max(covered_area, i+A[i]) #update this as most reach as possible.
        if i == last_jump_index:
            last_jump_index = covered_area
            number_of_jumps += 1
            if covered_area >= destination:
                return number_of_jumps
    return -1

# print(jump([2,1,1]))
print(jump([ 0, 46, 46, 0, 2, 47, 1, 24, 45, 0, 0, 24, 18, 29, 27, 11, 0, 0, 40, 12, 4, 0, 0, 0, 49, 42, 13, 5, 12, 45, 10, 0, 29, 11, 22, 15, 17, 41, 34, 23, 11, 35, 0, 18, 47, 0, 38, 37, 3, 37, 0, 43, 50, 0, 25, 12, 0, 38, 28, 37, 5, 4, 12, 23, 31, 9, 26, 19, 11, 21, 0, 0, 40, 18, 44, 0, 0, 0, 0, 30, 26, 37, 0, 26, 39, 10, 1, 0, 0, 3, 50, 46, 1, 38, 38, 7, 6, 38, 27, 7, 25, 30, 0, 0, 36, 37, 6, 39, 40, 32, 41, 12, 3, 44, 44, 39, 2, 26, 40, 36, 35, 21, 14, 41, 48, 50, 21, 0, 0, 23, 49, 21, 11, 27, 40, 47, 49 ]))