import numpy as np

# works for literally almost every test case
# def scramble(s1, s2):
    
#     # return ''.join([char for char in s2 if char in s1])
#     return True if s2 == ''.join([char for char in s2 if char in s1]) else False

# def scramble(s1, s2):
#     str1 = dict()
#     str2 = dict()


# print(scramble('dgggoffffg','dog' ))

# i,j = 'rkqodlww', 'world'
# def scramble(s1,s2):
#     str1 = list(s1)
#     if len(s1) < len(s2):
#         return False
#     for char in list(s1):
#         if char not in list(s2):
#             str1.remove(char)
#     for char in str1:
#         if s1.count(char) != s2.count(char):
#             return False
#         else:return True
    
    # for char in s2:
    #     if s2.count(char) != s1.count(char):
    #         return False
    #     else: return True

    

# def scramble(s1,s2):
#     # s1 = sorted(s1)
#     # s2 = sorted(s2)
#     if len(s1) < len(s2):
#         return False
#     for char in s2:
#         if char not in s1 or s1.count(char) < s2.count(char):
#             return False
#         elif s1.count(char) == 0:
#             return False

# print(scramble('katas', 'steak'))


#  Happen to be the only way that was the best, numpy.nditer is a super efficient way to iterate over an object
# def scramble(s1,s2):
#     for char in str(np.nditer(s2)):
#         if s1.count(char) < s2.count(char):
#             return False
#     else: return True

# def scramble(s1,s2):
#     while True:
#         try:
#             char = next(iter(s2))
#             if s1.count(char) < s2.count(char):
#                 return False
#         except StopIteration:
#             return True
#             break

# print(scramble('clonuqmpbgme', 'zmlwzkgszqwm'))


# print(''.join(sorted(i)) + '\n', ''.join(sorted(j)))


# Finally passed all 520 cases with a time of 3028ms first full pass and fast time doing so

from numpy import nditer 

def scramble(s1,s2):
    for char in str(nditer(s2)):
        if s1.count(char) < s2.count(char):
            return False
    else: return True

# lmao this was literally like everyones solution,
# so close to this but never 
# though to use set at all, neither did  
# I think it would have been any 
# faster then iterating over a string

# def scramble(s1,s2):
#     return all( s1.count(x) >= s2.count(x) for x in set(s2))