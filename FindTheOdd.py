def find_it(seq):
    Hash = dict()

    odd_num = None
    
    if len(seq) == 1:
        return seq[0]
    
    for i in range(len(seq)):
        Hash[seq[i]] = Hash.get(seq[i],0) + 1
    
    for i in Hash:
        if (Hash[i]%2 != 0):
            return i
    return odd_num
