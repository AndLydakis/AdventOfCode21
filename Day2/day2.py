#!/usr/bin/env python

def day2():
    x = 0
    depth = 0
    with open('input.txt', 'r') as input_:
        while True:
            nl = input_.readline().strip()
            if nl == '':
                print(depth * x)
                return()
            input_arr = nl.split(' ')
            print(input_arr)
            if input_arr[0] == 'forward':
                x += int(input_arr[1])
            elif input_arr[0] == 'down':
                depth += int(input_arr[1])
            else:
                depth -= int(input_arr[1])


if __name__ == '__main__':
    day2()