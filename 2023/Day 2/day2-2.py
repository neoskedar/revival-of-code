file1 = open('input.txt', 'r')
Lines = file1.readlines()
lst = []
start = 5
code = []


def get_next_number(start, direction):
    match direction:
        case "R":
            if start == 1 or start == 4 or start == 9 or start == 12 or start == 13:
                return start
            elif start == 2 or start == 3 or start == 5 or start == 6 or start == 7 or start == 8 or start == 10 or start == 11:
                return start + 1
        case "L":
            if start == 1 or start == 2 or start == 5 or start == 10 or start == 13:
                return start
            elif start == 3 or start == 4 or start == 6 or start == 7 or start == 8 or start == 9 or start == 11 or start == 12:
                return start - 1
        case "U":
            if start == 1 or start == 2 or start == 4 or start == 5 or start == 9:
                return start
            elif start == 3 or start == 13:
                return start - 2
            elif start == 6 or start == 7 or start == 8 or start == 10 or start == 11 or start == 12:
                return start - 4
        case "D":
            if start == 5 or start == 9 or start == 10 or start == 12 or start == 13:
                return start
            elif start == 1 or start == 11:
                return start + 2
            elif start == 2 or start == 3 or start == 4 or start == 6 or start == 7 or start == 8:
                return start + 4


def number_to_letter(number):
    match number:
        case 1:
            return "1"
        case 2:
            return "2"
        case 3:
            return "3"
        case 4:
            return "4"
        case 5:
            return "5"
        case 6:
            return "6"
        case 7:
            return "7"
        case 8:
            return "8"
        case 9:
            return "9"
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"


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
        code.append(number_to_letter(start))

print("Code: ", code)
