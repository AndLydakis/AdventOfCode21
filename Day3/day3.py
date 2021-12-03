#!/usr/bin/env python

def part1():
    counts = [0 for x in range(12)]
    
    with open('input.txt', 'r') as input_:
        while True:
            nl = input_.readline().strip()
            print(nl)
            if nl == '':
                epsilon_rate = ''
                gamma_rate = ''
                for i in range(len(counts)):
                    if counts[i] < 0:
                        gamma_rate += '0'
                        epsilon_rate += '1'
                    else:
                        gamma_rate += '1'
                        epsilon_rate += '0'
                print('Gamma Rate: ', gamma_rate, ' --> ', int(gamma_rate, 2))
                print('Epsilon Rate: ', epsilon_rate, ' --> ', int(epsilon_rate, 2))
                print('Power Consumption: ', int(epsilon_rate, 2) * int(gamma_rate, 2))
                return
            else:
                for c in range(len(nl)):
                    if int(int(nl[c]) == 0):
                        counts[c] -= 1
                    else:
                        counts[c] += 1
        


def part2():
    counts = [0 for x in range(12)]
    
    oxy_lines = []
    co2_lines = []
    with open('input.txt', 'r') as input_:
        while True:
                nl = input_.readline().strip()
                if nl == '':
                    break
                oxy_lines.append(nl)
                co2_lines.append(nl)

    num_lines = len(oxy_lines)
    num_digits = len(oxy_lines[0])

    for i in range(num_digits):
        count_0 = 0
        count_1 = 0
        print('--------')
        print(oxy_lines)
        print(co2_lines)
        print('--------')
        valid_oxy_idx = []
        valid_co2_idx = []
        if len(oxy_lines) > 1:
            for j in range(len(oxy_lines)):
                current_bit = oxy_lines[j][i]
                if current_bit == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            if count_0 > count_1:
                most_common = '0'
            else:
                most_common = '1'
            for j in range(len(oxy_lines)):
                if oxy_lines[j][i] == most_common:
                    valid_oxy_idx.append(j)
            print('valid oxy idx: ', valid_oxy_idx)
            oxy_lines = [oxy_lines[x] for x in valid_oxy_idx]
        

        count_0 = 0
        count_1 = 0
        if len(co2_lines) > 1:
            for j in range(len(co2_lines)):
                current_bit = co2_lines[j][i]
                if current_bit == '0':
                    count_1 += 1
                else:
                    count_0 += 1
            if count_0 >= count_1:
                most_common = '0'
            else:
                most_common = '1'
            for j in range(len(co2_lines)):
                if co2_lines[j][i] == most_common:
                    valid_co2_idx.append(j)
            print('valid co2 idx: ', valid_co2_idx)
            co2_lines = [co2_lines[x] for x in valid_co2_idx]
        
        print(co2_lines[0], '->', int(co2_lines[0], 2))
        print(oxy_lines[0], '->', int(oxy_lines[0], 2))
        print('Life support rating: ', int(co2_lines[0], 2) * int(oxy_lines[0], 2))

if __name__ == '__main__':
    # part1()
    part2()