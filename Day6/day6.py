#!/usr/bin/env python
from tqdm import tqdm
from collections import defaultdict

def day6(part2=False):
    fish = defaultdict(int)
    with open('input.txt') as input_file:
        for x in input_file.readline().strip().split(','):
            fish[int(x)] += 1
    print('Initial state: ', fish)

    for i in tqdm(range(256)):
        new_fish = fish[0]
        for j in range(8):
            fish[j] = fish[j+1]
        fish[6] += new_fish
        fish[8] = new_fish
    print('After ', i + 1, ' day(s): ', sum([fish[k] for k in fish]), ' fish')

if __name__ == '__main__':
    day6()