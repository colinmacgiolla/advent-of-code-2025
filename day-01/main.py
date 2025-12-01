
#!/bin/python


class CircularSequence:
    def __init__(self, position=50, size=100):
        self.size = size
        self.position = position 

    def move_forward(self, steps=1):
        wrap = 0
        estimate = self.position + steps
        if estimate >= self.size:
            wrap = estimate // self.size

        self.position = (self.position + steps) % self.size
        if self.position == 0:
            wrap += 1

        return self.position, wrap

    def move_backward(self, steps=1):
        wrap = 0
        estimate = self.position - steps
        if estimate < 0:
            wrap = (-estimate + self.size -1) // self.size

        self.position = (self.position - steps) % self.size
        if self.position == 0:
            wrap += 1
        return self.position, wrap

    def get_current(self):
        return self.position



def main():

    with open('.//input//data.txt') as f:
        raw_input = f.read()


    data = []

    for line in raw_input.split('\n'):
        if not line == '':
            data.append ( (line[0], line[1:]) )

    password_part_1 = 0
    password_part_2 = 0

    safe = CircularSequence()

    for entry in data:
        if entry[0] == 'R':
            resp = safe.move_forward(int(entry[1]))
        else:
            resp = safe.move_backward(int(entry[1]))
        
        if safe.get_current() == 0:
            password_part_1 += 1
        
        #password_part_2 += resp[1]

    # Brute force part 2
    start = 50
    password_part_2 = 0
    for entry in data:
        turns, move = divmod(int(entry[1]), 100)
        password_part_2 += turns
        if entry[0] == 'R':
            if start + move >= 100:
                password_part_2 += 1
        else:
            if start > 0 and (start - move) <= 0:
                password_part_2 += 1
        
        if entry[0] == 'R':
            start = (start + move) % 100
        else:
            start = (start + move * -1) % 100 

    print(f"Part 1 password is: {password_part_1}")
    print(f"Part 2 password is: {password_part_2}")
    print("End of line.")
    return 0

if __name__ == "__main__":
    main()