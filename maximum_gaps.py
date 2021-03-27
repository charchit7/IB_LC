def mg(arr):
    bucket = [float('inf'), -float('inf')]
    buckets = [bucket]* len(arr)

    maximum = max(arr)
    minimum = min(arr)

    for number in arr:
        index = (number-minimum) * (len(arr)-1) // (maximum - minimum)
        current_Bucket = buckets[index]
        # print(current_Bucket)
        buckets[index] = [min(number, current_Bucket[0]), max(number, current_Bucket[1])]
    # print(buckets)
    cleanedBucket= list(filter(lambda x: x[0] != float('inf') or x[1] != -float('inf'), buckets))
    # print(cleanedBucket)

    res = 0
    for i in range(1,len(cleanedBucket)):
        res = max(res, cleanedBucket[i][0] - cleanedBucket[i-1][1])
    return res


print(mg([3,6,9,1]))
print(mg([10]))