import re


def create_phone_number(n):
    num = ""
    for i in n:
        num = num + str(i)

    match = " ".join('(%s) %s-%s' %
                     tuple(re.findall(r'\d{4}$|\d{3}', num))).split()
    match.insert(5, " ")
    result = ""

    for i in match:
        result = result + str(i)

    return result


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
