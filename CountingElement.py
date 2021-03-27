def CountElement(tempArr):
    arr = set(tempArr)
    count = 0
    for element in tempArr: 
        if element + 1 in arr:
            count += 1
    return count


arr = [1,2,3]
arr2 = [1,1,3,3,5,5,7,7]
arr3 = [1,1,2,2]
arr4 = [1,3,2,3,5,0]
print(CountElement(arr))
print(CountElement(arr2))
print(CountElement(arr3))
print(CountElement(arr4))
