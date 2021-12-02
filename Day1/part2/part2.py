#!/usr/bin/env python

def day2():
    cnt = 0
    input = open('input.txt', 'r')
    input_list = []
    for line in input:
        if line != '':
            input_list.append(int(line))
    cur_sum = 0
    for i in range(3):
        cur_sum += input_list[i]
    for i in range(1, len(input_list)-2):
        new_sum = 0
        for j in range(i, i+3):
            print(j, input_list[j])
            new_sum += input_list[j]
        print('Cur Sum:', cur_sum, ' New sum: ', new_sum)
        if new_sum > cur_sum:
            cnt += 1
        cur_sum = new_sum
    print(cnt)

if __name__ == '__main__':
    day2()