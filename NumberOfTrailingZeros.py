def zeros(num):
    #     facts = [x for x in range(1,num+1)]
    firstZero = int(num/5)
    secondDigit = int(firstZero/5)

    return firstZero + secondDigit

    



# def zeros(num):
#     facts = [x for x in range(1,num+1)]

#     left = (num / 5) if num % 5 == 0 else None

#     zero = (left + (num / 5)) if left != None else None

#     return zero if zero != None else None
