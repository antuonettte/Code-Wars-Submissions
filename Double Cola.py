import itertools as t
import math

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

# def who_is_next(names, r):
#     names.extend([names[0],names[0]])
#     names.pop(0)
    
#     if r == 0:
#         return names[-3]
#     else:
#         return who_is_next(names,r-1)


# Very Clever way to solve with recursion, but python recursive depth hit too early.

# def who_is_next(names, r):

#     for x in range(r):
#         names.extend([names[0],names[0]])
#         names.pop(0)

#     return names[-3]
# figure out how this way works

# another way without recursion, but still too slow for codewars, I have to find a way using math
def who_is_next(names, r):
    line = len(names)
    while r > line:
        r-=line
        line*=2
    return names[math.ceil(r/(line/len(names)))-1]
    





print(who_is_next(names, 7230702951))