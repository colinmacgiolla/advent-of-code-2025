#!/bin/python
import re

def expand(data:str ):

    dataSet = set()
    stripped_list = [entry.strip() for entry in data.split(',')]
    for entry in stripped_list:
        if '-' in entry:
            # expand
            data_range = entry.split('-')
            expanded = set( range( int(data_range[0]),int(data_range[1])+1) )
            dataSet.update(expanded)

        else:
            dataSet.add( int(entry) )

    return  list(dataSet)


def has_repeated_pattern(num):
    s = str(num)

    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    return first_half == second_half, num

def part_2(num):
    s = str(num)
    
    match = re.search(r'^(\d+?)\1+$', s)
    if match:
        return True, match.group(1)
    else:
        return False, None


def main():

    with open('.//day-02//input//data.txt') as f:
        raw_input = f.read()

    data = expand(raw_input)

    result_1 = 0
    result_2 = 0

    for entry in data:
        if len(str(abs(entry))) % 2 == 0:
            repeats, number = has_repeated_pattern(entry)
            if repeats:
                result_1 += number

        repeats, number = part_2(entry)
        if repeats:
            result_2 += entry


    print(f"Part 1 result: {result_1}")
    print(f"Part 2 result: {result_2}")
    print("End of line.")
    return 0

if __name__ == "__main__":
    main()