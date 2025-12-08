#!/bin/python

import re

def part_1(data):
    operands = []
    operators = []

    for line in data[:-1]:
        numbers = re.findall(r"\d+", line)
        operands.append(numbers)
    
    operators = re.split(r"\s+", data[-1])

    result = 0

    for index, operator in enumerate(operators[:-1]):
        value = 0
        if operator == '+':
            for entry in operands:
                value += int(entry[index])
        else:
            for entry in operands:
                if value == 0:
                    value = 1
                value = value * int(entry[index])
        result += value
    
    return result


def part_2(data):
    operands = []
    results = []
    
    transposed = [list(row) for row in zip(*data)]

    result = 0
    for line in transposed:
        if not all(c==' ' for c in line[:-1]): 
            operands.append(int("".join(map(str, line[:-1]))))
            if line[-1] != ' ':
                operator = line[-1]
        else:
            for entry in operands:
                if operator == '+':
                    result += entry
                else:
                    if result == 0:
                        result = 1
                    result = result * entry
        
            results.append(result)
            operands.clear()
            result = 0

    for entry in operands:
        if operator == '+':
            result += entry
        else:
            if result == 0:
                result = 1
            result = result * entry

    results.append(result)

    return sum(results)
        



def main():

    with open('.//day-06//input//data.txt') as f:
        raw_input = f.read()

    data = []

    for line in raw_input.split('\n'):
        if not line == '':
            data.append(line)

    result_1 = part_1(data)

    print(f"Part 1 result: {result_1}")
    print(f"Part 2 result: {part_2(data)}")
    print("End of line.")
    return 0

if __name__ == "__main__":
    main()