A = [ [0] ]
B = 2

def search(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j])
            if arr[i][j] == target:
                return (i+1)*1009 + (j+1)
    return -1


print(search(A,B))
#you can use binary search for faster searching

