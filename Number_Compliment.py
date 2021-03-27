# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), 
# and its complement is 010. So you need to output 2.


# # def number_to_binary(num):
# #     arr = [0] * (num//3)
# #     counter = 0
# #     while num > 0:
# #         arr[counter] = num % 2
# #         num = num//2
# #         counter += 1
# #     return arr

# # def n_to_b(num):
# #     a = (bin(num)[2:])   
# #     for i in a:
# #         if i == 1: return 0
# #         else: return 1


#the idea here is that number complimented with its compliment is 11111
#so if we compliment that number with 1111 will get the compliemnt of nimber
def findComplement(num: int) -> int:
    number_just_greater = 0
    while num > number_just_greater:
        number_just_greater = 2*number_just_greater + 1
        print(number_just_greater)
    return number_just_greater^num

print(findComplement(7))

#1 liner    
#return num^(2**(len(bin(num)[2:]))-1)