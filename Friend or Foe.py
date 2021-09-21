def friend(list):
    return [x for x in list if len(x) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))
