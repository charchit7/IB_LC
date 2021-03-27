# Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# # means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

def backspaceCompare(S,T):
    i = len(S) - 1 
    j = len(T) - 1
    skipS = 0
    skipT = 0

    while (i >= 0 or j >= 0):  # While there may be chars in build(S) or build (T)....
        while (i >= 0): #Find position of next possible char in build(S)...
            if (S[i] == '#'):
                skipS +=1
                i -=1
            elif (skipS > 0):
                skipS -=1 
                i -=1
            else:
                break

        while (j >= 0):#Find position of next possible char in build(T).....
            if (T[j] == '#'):
                skipT +=1
                j -=1
            elif (skipT > 0):
                skipT -= 1 
                j -= 1
            else:
                break
        
        #// If two actual characters are different
        print('value of i , j at that point',i,j)
        if (i >= 0 and j >= 0 and S[i] != T[j]):
            print('first if statement')
            return False
        #// If expecting to compare char vs nothing
        if ((i >= 0) != (j >= 0)):
            print((i >= 0))
            print('second if statement')
            return False
        i -= 1 
        j -= 1
    return True

# print(backspaceCompare('ABC##', 'ABCD##'))

print(backspaceCompare('ABC###', 'ABC##'))


S = "ab#c"
T = "#ad#c"


def modify(text):
    temp = []
    for i in text:
        if i!= '#':
            temp.append(i)
        else:
            if temp:
                temp.pop()
    return temp

def testing(a1,a2):
    temp1 = modify(a1)
    temp2 = modify(a2)
    print(temp2)

    return temp1 == temp2

print(testing(S,T))

################################
S = "ab#c" 
T = "ad#c"

x = "y#fo##f"
y = "y#f0#0#f"

from itertools import zip_longest

def res(str):
    skip = 0
    for i in reversed(str):
        if i =='#':
            skip += 1
        elif skip>0:
            skip -= 1
        else:
            yield i

def backspace_compare(a,b):
    return all(p==q for p,q in zip_longest(res(a),res(b)))

# print(backspace_compare(x,y))
# print(backspace_compare(S,T))

