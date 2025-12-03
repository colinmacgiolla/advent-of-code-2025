#!/bin/python


def max_sequence(s, digits=12):
    stack = []
    to_remove = len(s) - digits

    for digit in s:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    result = ''.join(stack[:12])
    return result


def main():

    with open('.//day-03//input//data.txt') as f:
        raw_input = f.read()

    data = []

    for line in raw_input.split('\n'):
        if not line == '':
            data.append(line)

    results_1 = []
    results_2 = []

    for bank in data:
        joltage = ""

        # Find the highest charge in the bank, excluding the last digit, since we need at
        # least one more digit to the right.

        # This passes, but only really works like this for 2 digit numbers, since we search for
        # the highest number that isn't the last, then search from that number to the end for the 
        # 2nd digit.
        index, charge = max(enumerate(bank[:-1]), key=lambda t: t[1])
        joltage += charge
        remainder = bank[index+1:]
        index, charge = max(enumerate(remainder), key=lambda t: t[1])
        joltage += charge

        results_1.append(joltage)
        results_2.append(max_sequence(bank))

    print(f"Part 1 result: {sum(map(int,results_1))}")
    print(f"Part 2 result: {sum(map(int,results_2))}")
    print("End of line.")
    return 0


if __name__ == "__main__":
    main()
