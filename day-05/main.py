#!/bin/python


def part_1(fresh, ingredients):

    is_fresh = []

    for ingredient in ingredients:
        if any(start <= ingredient <= end for start, end in fresh):
            is_fresh.append(ingredient)
        else:
            pass
    
    return is_fresh


def part_2(fresh):
    ctr = 0
    n = 0

    for start, end in sorted(fresh):
        new_n = max(n, end)
        if start <= n:
            ctr += new_n - n
        else:
            ctr += end - start + 1
        n = new_n
        
    return ctr



def main():


    with open('./day-05/input/data.txt') as f:
        raw_input = f.read()

    fresh = []
    ingredients = []

    for line in raw_input.split('\n'):
        if not line == '':
            if '-' in line:
                fresh.append( tuple(int(x) for x in line.split('-')) )
            else:
                ingredients.append(int(line))

        
    print(f"Part 1 result is: { len(part_1(fresh, ingredients))}")
    print(f"Part 2 result is: { part_2(fresh)}")
    print("End of line.")
    return 0


if __name__ == "__main__":
    main()