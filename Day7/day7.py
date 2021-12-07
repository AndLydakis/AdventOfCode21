#!/usr/bin/env python
from tqdm import tqdm
from collections import defaultdict
import sys

def part1():
    print('Part 1')
    with open('input.txt') as input_file:
        crabs = [int(x) for x in input_file.readline().strip().split(',')]
    
    crabs = sorted(crabs)
    # print(crabs)
    modCrabs = crabs.copy()
    modCrabsEven = crabs.copy()
    num_crabs= len(crabs)
    mid = crabs[int(num_crabs/2)]
    cost = 0
    for i in tqdm(range(num_crabs)):
        inc = abs(crabs[i] - mid)
        if (crabs[i] < mid):
            modCrabs[i] += inc
        else:
            modCrabs[i] -= inc
        cost += abs(inc)
    if num_crabs % 2 == 0:
        even_cost = 0
        mid = crabs[int(num_crabs/2) - 1]
        c = 0
        for i in tqdm(range(num_crabs)):
            inc = abs(crabs[i] - mid)
            even_cost += abs(inc)
        cost = min(cost, even_cost)
        if even_cost < cost:
            # print(modCrabsEven)
            print(cost)
    # print(modCrabs)
    print(cost)

def part2():
    print('Part 2')
    with open('input.txt') as input_file:
        crabs = [int(x) for x in input_file.readline().strip().split(',')]

    num_crabs = len(crabs)
    avg = int(sum(crabs) / num_crabs)
    
    cost = 0
    cost_even = 0

    for i in tqdm(range(num_crabs)):
        c = crabs[i]
        cost += abs(avg - c) * (abs(avg - c) + 1) / 2
        cost_even += abs(avg + 1 - c) * (abs(avg + 1 - c) + 1) / 2

    print("Cost: ", cost)
    print("Even Cost: ", cost_even)
    print("Min Cost: ", min(cost, cost_even))

if __name__ == '__main__':
    part1()
    part2()