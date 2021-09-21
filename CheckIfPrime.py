from math import sqrt

def is_prime(num):
    if num <= 1: return False

    for n in range(2,int(sqrt(num)) + 1):
        if num % n == 0:
            return False
        else: continue
    else:
        return True



# from math import floor as f
# from math import sqrt

# def is_prime(num):
#     if num <= 1: return False
#     root = int(sqrt(num))

#     for n in range(2,root + 1):
#         if num % n == 0:
#             return False
#         else: continue
#     else:
#         return True


