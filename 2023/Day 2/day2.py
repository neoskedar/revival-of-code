file1 = open('input.txt', 'r')
Lines = file1.readlines()
lst = []
start = 5
code = []


def get_next_number(start, direction):
    match direction:
        case "R":
            if start == 3 or start == 6 or start == 9:
                return start
            else:
                return start + 1
        case "L":
            if start == 1 or start == 4 or start == 7:
                return start
            else:
                return start - 1
        case "U":
            if start == 1 or start == 2 or start == 3:
                return start
            else:
                return start - 3
        case "D":
            if start == 7 or start == 8 or start == 9:
                return start
            else:
                return start + 3


count = 0
# Strips the newline character
for line in Lines:
    for letter in line:
        lst.append(letter)
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    print(lst)

for x in lst:
    if x == "R":
        print("right")
        start = get_next_number(start, x)
    elif x == "L":
        print("left")
        start = get_next_number(start, x)
    elif x == "U":
        print("up")
        start = get_next_number(start, x)
    elif x == "D":
        print("down")
        start = get_next_number(start, x)
    else:
        code.append(start)
        print("Current number: ", start)

print("Code: ", code)
