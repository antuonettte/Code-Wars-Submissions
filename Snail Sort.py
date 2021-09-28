from itertools import chain

def snail(arr):
    mid = list(map(lambda row : row[slice(1, len(row)-1)], arr[slice(1,len(arr)-1)]))


    return list(chain.from_iterable([
        arr[0],
        list(map(lambda row: row[len(row)-1], arr[slice(1,len(arr)-1)])),
        list(reversed(arr[len(arr)-1])) if len(arr) > 1 else [],
        list(map(lambda row: row[0],list(reversed(arr[slice(1,len(arr)-1)])))),
        snail(mid) if len(mid) > 0 else []

     ]))if len(arr) >= 1 else [[]]


     
arr = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(arr))

