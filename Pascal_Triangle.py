# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

def pas(num):
    res = [[1]]
    elem = []
    counter = 1
    while counter<num:
        for i in range(counter):
            if i == 0:
                elem.append(1)
            else:
                elem.append(res[-1][i-1] + res[-1][i])
        elem.append(1)
        res.append(elem)
        elem = []
        counter += 1
    return res
print(pas(100))

#####################################################################
def generate(self, numRows):
        res = [[1]]
        for _ in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
########################################################################


"""
O(k) extra space only 
"""
#######################################################################
class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex==0: return [1]
        #if rowIndex==1: return [1,1]
        
        prev=[1,1]
        #[1,2,1] #[1,3,3,1]
        
        for row in range(1,rowIndex+1):
            ans=[1]
            for i in range(1,row):
                ans.append(prev[i-1]+prev[i])
            ans.append(1)
            prev=ans
            
        return prev 
#########################################################################

def generate(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle