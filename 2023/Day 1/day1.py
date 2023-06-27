# https://adventofcode.com/2016/day/1
test_data = ["R2", "L3"]
test_data2 = ["R2", "R2", "R2"]
test_data3 = ["R5", "L5", "R5", "R3"]
test_data4 = ["L1", "L5", "R1", "R3", "L4", "L5", "R5"]
direction = 0
distance = 0
turn = 0
current = 0

# open file
f = open("input.txt", "r")

# read file
input = f.read()

# split input into array
input = input.split(", ")

for x in test_data4:
    print("Direction: ", x[0][0], x[1][0])
    if x[0][0] == "R":
        turn = 0
    else:
        turn = 1

    if turn == 0:
        direction += 1
    else:
        direction -= 1

    if direction > 3:
        direction = 0

    if 1 >= direction >= -1:
        distance += int(x[1:])
    else:
        distance -= int(x[1:])

    print("Total distance: ", distance)
