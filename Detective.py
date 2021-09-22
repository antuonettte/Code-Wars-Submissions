import itertools as tool


def get_pins(observed):
    nums = {
        '1' : ['1','2','4'],
        '2' : ['2','1','3','5'],
        '3' : ['2','6','3'],
        '4' : ['1','5','7','4'],
        '5' : ['2','4','6','8','5'],
        '6' : ['3','5','9','6'],
        '7' : ['4','8','7'],
        '8' : ['7','5','9','0','8'],
        '9' : ['6','8','9'],
        '0' : ['8','0']
        }
    
    x = [nums [i] for i in observed ]
    y = list(tool.product(*x))
    return [''.join(x) for x in y]


print(get_pins('123'))

    


