#for small arrays less than 20-30 elements both insertion sort and selection sort are faster than the )(n*logn) alternatives..

# Usually, insertion sort will perform less comparisons than selection sort, depending on the degree of "sortedness" of the array. While selection sort must scan 
# the remaining parts of the array when placing an element, insertion sort only scans as many elements as necessary. 
# That means that when the array is already sorted or almost sorted, insertion sort performs in O(n) time.

# One advantage of selection sort over insertion sort, is that the number of writes (swaps) is in O(n), while in insertion sort it is in O(n^2). 
# This may be important if you are sorting on Flash memory, for example, because writes reduce the lifespan of Flash memory.

# If the list is almost sorted, then Insertion Sort performs in linear O(n) time. Contrast this with Selection Sort, which always performs in quadratic time.

nums = [5,4,3,2,1]

#selection sort

#find the min index function
def min_index(arr,start,end):
    min_ind = start
    for i in range(start+1,end):
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind

# if the value at min index doesen't match with the value at the current index
# swap the value at those indexes.
def selection_sort(arr):
    for i in range(len(arr)):
        minid = min_index(arr,i,len(arr))
        if i != minid:
            arr[i], arr[minid] = arr[minid], arr[i]
    return arr

print(selection_sort(nums))
