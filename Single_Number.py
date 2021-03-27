def Single_Number(arr):
    answer = 0
    for num in arr:
        answer = answer^num
        print(answer)
    return answer
arr = [3,1,1,2,2]
print(Single_Number(arr))