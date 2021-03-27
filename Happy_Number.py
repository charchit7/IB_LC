"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the 
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Input: 19
Output: true
Explanation: 
1*2 + 9*2 = 82
8*2 + 2*2 = 68
6*2 + 8*2 = 100
1*2 + 0*2 + 02 = 1

"""

def isHappy(n) -> bool:
    answer = 0  
    temp = 0
    while answer != 1:
        for i in str(n):
            temp += int(i)**2
        answer += temp
        if answer == 4:
            return False
        return True
        
print(isHappy(19))
print(isHappy(3))


"""
#Floyd Cycle Detection Algorithm
int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow, fast;
    slow = fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while(slow != fast);
    if (slow == 1) return 1;
    else return 0;
}
"""


