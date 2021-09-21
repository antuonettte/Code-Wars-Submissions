def duplicate_encode(word):
    return ''.join(["(" if word.count(x.lower()) == 1 else ")" for x in word])

# print(duplicate_encode(") )TBnZU)Xyy Dt)BaWhZhHYo"))

# print(duplicate_encode("recede"))

test = "J)(!"

print(test.count(''))