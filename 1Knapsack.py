def knapsack(value_array,weight_array, capacity,n):
    if n == 0 or capacity == 0:
        return 0
    
    if weight_array[n-1] <= capacity:
        return max(value_array[n-1] + knapsack(value_array,weight_array,capacity- weight_array[n-1],n-1), knapsack(value_array,weight_array,capacity,n-1))
    elif weight_array[n-1] > capacity:
        return knapsack(value_array,weight_array,capacity,n-1)


A = [60, 100, 120]
B = [10, 20, 5]
C = 15

# print(knapsack(A,B,C,3))

# A = [ 468, 335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323 ]
# B = [ 4, 4, 5, 2, 2, 4, 9, 8, 5, 3, 8, 8, 10, 4, 2, 10, 9, 7, 6, 1, 3, 9, 7, 1, 3, 5, 9, 7, 6, 1, 10, 1, 1, 7, 2, 4, 9, 10, 4, 5, 5, 7 ]
# C = 841



#this method works because of top down approach , iterative dp
def knapsack1(value_arr, wht_arr, capacity, n):
    dp = [[-1 for i in range(capacity+1)] for i in range(n+1)]
    
    #fill the base cases, ie, if capacity = 0 and n = 0 return 0 so we 
    # fill the 0 ros and 0 column with 0.

    #fill the column or say the height
    for i in range(1):
        for j in range(capacity+1):
            dp[i][j] = 0

    #fill the first row
    for i in range(1):
        for j in range(n+1):
            dp[j][i] = 0

    #fill the remaining data in the array
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if wht_arr[i-1] <= j:
                dp[i][j] = max(value_arr[i-1]+ dp[i-1][j-wht_arr[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp

# A = [ 468, 335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323 ]
# B = [ 4, 4, 5, 2, 2, 4, 9, 8, 5, 3, 8, 8, 10, 4, 2, 10, 9, 7, 6, 1, 3, 9, 7, 1, 3, 5, 9, 7, 6, 1, 10, 1, 1, 7, 2, 4, 9, 10, 4, 5, 5, 7 ]
# C = 841

# print(knapsack1(A,B,C,len(A)))

A = [60, 100, 120]
B = [10, 20, 5]
C = 15
print(knapsack1(A,B,C,len(A)))
