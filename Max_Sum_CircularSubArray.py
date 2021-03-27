arr = [3,-1,2,-1]

def circular_subarray(arr):
    #we have two cases where is first case we have the max_subarray in the middle so that can be
    #easily solved using the kadane's algo
    #second case where first element and the last element comprises the max_val in that case 
    # we use formula max(maxSum , total - minSum)

    total = 0
    curMax = 0
    curMin = 0
    sum_Max = arr[0]
    sum_Min = arr[0]

    for a in arr:
        curMax = max(curMax+a, a)
        sum_Max = max(curMax, sum_Max)
        curMin = min(curMin + a, a)
        sum_Min = min(curMin, sum_Min)
        total += a
    print(sum_Min, total)

    return max(sum_Max, total - sum_Min) if sum_Max > 0 else sum_Max

print(circular_subarray(arr))
