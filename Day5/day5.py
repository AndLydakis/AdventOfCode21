#!/usr/bin/env python
from collections import defaultdict


def day5(part2=False):
    with open('input.txt') as input_file:
        covering = defaultdict(int)

        for line in input_file:
            pair = line.strip().split(' -> ')
            start = [int(x) for x in pair[0].split(',')]
            end = [int(x) for x in pair[1].split(',')]

            if start[0] == end[0]:  # same x
                for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    # print('Increasing ', start[0], y)
                    covering[(start[0], y)] += 1
            elif start[1] == end[1]:  # same y
                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    # print('Increasing ', x, start[1])
                    covering[(x, start[1])] += 1
            elif part2:  # diagonal
                if start[0] < end[0]:
                    rx = range(start[0], end[0] + 1)
                else:
                    rx = range(start[0], end[0] - 1, -1)

                if start[1] < end[1]:
                    ry = range(start[1], end[1] + 1)
                else:
                    ry = range(start[1], end[1] - 1, -1)

                for x, y in zip(rx, ry):
                    covering[(x, y)] += 1

        print("Sum : ", sum([1 for i in covering if covering[i] > 1]))


if __name__ == '__main__':
    day5(part2=True)
