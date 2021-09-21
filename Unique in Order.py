from itertools import groupby


def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
    # new_list = []
    # currentItem = None
    # for idx, items in enumerate(iterable):
    #     if items != currentItem:
    #         new_list.append(items)
    #         currentItem = items
    #     else:
    #         continue

    # return new_list


print(unique_in_order('AAAABBBCCDAABBB'))
