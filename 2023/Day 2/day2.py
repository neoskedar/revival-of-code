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

for line in Lines:
    for letter in line:
        lst.append(letter)

for x in lst:
    if x == "R":
        start = get_next_number(start, x)
    elif x == "L":
        start = get_next_number(start, x)
    elif x == "U":
        start = get_next_number(start, x)
    elif x == "D":
        start = get_next_number(start, x)
    else:
        code.append(start)

code.append(start)
print("Code: ", code)