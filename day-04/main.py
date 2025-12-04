#!/bin/python

max_x = 0
max_y = 0

    
def is_valid( coord, min_x=0, min_y=0):
    global max_x, max_y

    x,y = coord
    if x < min_x or x >= max_x:
        return False
    if y < min_y or y >= max_y:
        return False
    
    return True
    

def get_neighbours(position):
    moves = [ (-1,-1), (0,-1),(1,-1), (-1,0), (1,0), (-1,1), (0, 1), (1,1) ]
    neighbours = []

    for move in moves:
        neighbour = tuple(a + b for a,b in zip(position, move))
        if is_valid(neighbour):
            neighbours.append(neighbour)
    return neighbours


def part_1(grid):
    accessible = []

    for entry in grid:
        ctr = 0
        neighbours = get_neighbours(entry)
        for neighbour in neighbours:
            if neighbour in grid:
                ctr += 1
        if ctr < 4:
            accessible.append(entry)
    
    return accessible

def part_2(grid):

    ctr = 0
    accessible = part_1(grid)

    while len(accessible) > 0:
        ctr += len(accessible)
        grid.difference_update(set(accessible))
        accessible = part_1(grid)

    return ctr

    

def main():
    global max_x
    global max_y

    with open('./day-04/input/data.txt') as f:
        raw_input = f.read()
    raw_data = []

    grid = set()
    x,y = 0,0

    for line in raw_input.split('\n'):
        if not line == '':
            raw_data.append(line)


    for line in raw_data:
        for point in line:
            if point == '@':
                grid.add((x,y))
            x += 1
        x = 0
        y += 1
    
    max_x = len(line)
    max_y = y
    

    print(f"Part 1 result is: { len(part_1(grid)) }")
    print(f"Part 1 result is: { part_2(grid) }")

    print("End of line.")
    return 0


if __name__ == "__main__":
    main()
