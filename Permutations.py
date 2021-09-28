from itertools import permutations as p 
from pprint import pprint

def permutations(string):
        
    return set(''.join(word) for word in p(string, len(string)))

pprint(permutations('ABCD'))
