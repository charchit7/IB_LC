
def jump(nums):
    
    size = len(nums)
    
    # destination is last index
    destination = size - 1
    
    # record of current coverage, record of last jump index
    cur_coverage, last_jump_index = 0, 0
    
    # counter for jump
    times_of_jump = 0
    
        # Quick response if start index == destination index == 0
    if size == 1:
        return 0
    
    
    # Greedy strategy: extend coverage as long as possible with lazy jump
    for i in range( 0, size):
        
        # extend current coverage as further as possible
        cur_coverage = max( cur_coverage, i + nums[i] )
        

        # forced to jump (by lazy jump) to extend coverage  
        if i == last_jump_index:
        
            # update last jump index
            last_jump_index = cur_coverage
            
            # update counter of jump by +1
            times_of_jump += 1
            
            # check if reached destination already
            if cur_coverage >= destination:
                    return times_of_jump
            
    return times_of_jump


def jump1(nums):
    if len(nums)<2:
        return 0
    
    max_pos=nums[0]
    max_step=nums[0]
    jump=1
    for i in range(1,len(nums)):
        if max_step<i:
            jump+=1
            max_step=max_pos
        max_pos=max(max_pos,nums[i]+i)
    
    return jump