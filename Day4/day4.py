#!/usr/bin/env python

import numpy as np
from itertools import chain


def part1(part2=False):
    boards = []
    current_board = []
    with open('input.txt') as input_file:
        numbers = input_file.readline()
        input_file.readline()
        numbers = [int(x) for x in numbers.strip().split(',')]
        for line in input_file:
            # print('*', line)
            if line.strip() == '':
                if len(current_board) > 0:
                    boards.append(current_board)
                current_board = []
            else:
                current_board.append([int(x) for x in line.strip().replace('  ', ' ').split(' ')])
        boards.append(current_board)

        def check_board(i):
            current_board = boards[i]
            num_rows = len(current_board)
            num_cols = len(current_board[0])
            for row in range(num_rows):
                for col in range(num_cols):
                    if current_board[row][col] == num:
                        current_board[row][col] = -1
                        row_sums = [sum(r) for r in current_board]
                        col_sums = [sum(c) for c in zip(*current_board)]
                        if (-5 in row_sums) or (-5 in col_sums):
                            print("Board {}/{} wins".format(i + 1, len(boards)))
                            print(current_board)
                            res = 0
                            for j in range(num_cols):
                                for k in range(num_rows):
                                    if current_board[j][k] != -1:
                                        res += current_board[j][k]
                            res = sum(
                                [(0 if current_board[i][j] == -1 else current_board[i][j]) for i in range(5) for j
                                 in range(5)]
                            )
                            print('Points: {}'.format(res * num))
                            print('Last number was: {}'.format(num))
                            if not part2:
                                exit()
                            else:
                                return True

        winning_boards = []
        for num in numbers:
            for i in range(len(boards)):
                if i in winning_boards:
                    continue
                if check_board(i):
                    winning_boards.append(i)


if __name__ == '__main__':
    part1(part2=True)
