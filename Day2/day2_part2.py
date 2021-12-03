#!/usr/bin/env python

def day2():
    x = 0
    aim = 0
    depth = 0
    with open('input.txt', 'r') as input_:
        while True:
            nl = input_.readline().strip()
            if nl == '':
                print("Final value", depth * x)
                return()
            input_arr = nl.split(' ')
            cmd = input_arr[0]
            val = int(input_arr[1])
            if cmd == 'forward':
                x += val
                depth += aim * val
            elif cmd == 'down':
                aim += val
            else: #up
                aim -= val
            print('X: ', x, ', Aim: ', aim, ', Depth: ', depth)


if __name__ == '__main__':
    day2()