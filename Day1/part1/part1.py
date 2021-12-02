#!/usr/bin/env python

cnt = 0
input = open('input.txt', 'r')
cur = int(input.readline())
while True:
    new_line = input.readline().strip()
    if new_line == '':
        break
    n = int(new_line)
    if not n:
        break
    if n > cur:
        cnt += 1
    cur = n
print(cnt)
    