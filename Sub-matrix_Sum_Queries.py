A = [   [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]   ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]


#rowwise sum
def row_preffix_sum(arr):
    for i in arr:
        for j in range(1,len(i)):
            i[j] = i[j-1]+i[j]
    return arr

#columwise sum
def column_prefix_sum(arr):
    for i in range(len(arr)):
        

print(row_suffix_sum(A))