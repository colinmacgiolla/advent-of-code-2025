#!/bin/python

from collections import defaultdict

def main():

    with open('.//day-07//input//data.txt') as f:
        raw_input = f.read()

    grid = {}
    y = 0
    max_x = 0
    max_y = 0

    for line in raw_input.split('\n'):
        if not line == '':
            for index, val in enumerate(line):
                grid[(index, y)] = val
                if index == 0:
                    max_x = len(line)
            y += 1
    max_y = y

    splits = 0
    timeline = [0] * len(raw_input.split('\n')[0])

    for y in range(1, max_y):
        for x in range(0, max_x):
            if grid[(x,y-1)] == 'S' and grid[(x, y)] == '.':
                # only 1 way to get here
                timeline[x] = 1
                grid[(x, y)] = '|'

            elif grid[(x,y-1)] == '|' and grid[(x, y)] == '.':
                # just a decent
                grid[(x, y)] = '|'


            elif grid[(x, y-1)] == '|' and grid[(x, y)] == '^':
                splits += 1
                timeline[x-1] += timeline[x]
                timeline[x+1] += timeline[x]
                if grid[ (x-1,y)] == '.':
                    grid[ (x-1,y)] = '|'
                if grid[ (x+1, y) ] == '.':
                    grid[ (x+1,y)] = '|'
                    
                timeline[x] = 0



    print(f"Part 1 result: {splits}")
    print(f"Part 2 result: {sum(timeline)}")
    print("End of line.")
    return 0

if __name__ == "__main__":
    main()