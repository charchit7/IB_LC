# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true


# def checkStraightLine(coordinates):    
#     (x0, y0), (x1, y1) = coordinates[:2]
#     for x, y in coordinates:
#         print(x0, y0, x1, y1, x, y)
#         if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
#             return False
#     return True

print(check([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
