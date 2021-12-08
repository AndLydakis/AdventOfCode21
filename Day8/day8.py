#!/usr/bin/env python
from itertools import permutations

def day8():
    numbers = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'e'],
        2: ['a', 'c', 'e', 'd', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['c', 'b', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'f', 'g', 'e'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'd', 'c', 'e', 'f', 'g'],
        9: ['a', 'b', 'd', 'c', 'f', 'g'],
    }
    seen = {
        'a':'',
        'b':'',
        'c':'',
        'd':'',
        'e':'',
        'f':'',
        'g':'',
    }
    ps = permutations(*[seen.keys()])
    print([p for p in ps])
    with open('input.txt') as input_:
        l = input_.readline().strip().split('|')
        segments = [x for x in l[0].strip().split(' ')]
        output = [x for x in l[1].strip().split(' ')]
        print('Segments: ', segments)
        print('Output: ', output)

if __name__ == '__main__':
    day8()