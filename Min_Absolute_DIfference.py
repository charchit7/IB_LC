# given arr find the min absolute val of | A[i] - A[j] |

# max(list, key = abs)

A = [1,2,3,4,5]
B = [5, 17, 100, 11]


def min_abs(arr):
    arr.sort()
    minimum = float('inf')
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) < minimum:
            minimum = abs(arr[i] - arr[i+1])
    return minimum



print(min_abs(A))
print(min_abs(B))