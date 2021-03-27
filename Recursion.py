def fib(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number-2) + fib(number-1)


print(fib(8))
###########################################Better way Memoization #####
def fiboo(number,arr):
    if arr[number] != -1:
        return arr[number]
    else:
        arr[number] = fiboo(number-2, arr) + fiboo(number-1, arr)   
    return arr[number]

def fib_memo(number):
    num = [-1]*(number+1)
    num[0] = 0
    num[1] = 1
    return fiboo(number,num)
    
print(fib_memo(5))

################################  0/1 Knapsac ########################3

"""
#Note:- if you want to initialize a array with all zeroes then do, arr[:] = bytearray(size)

"""