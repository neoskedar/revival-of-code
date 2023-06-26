# https://adventofcode.com/2016/day/1
test_data = ["R2", "L3"]
test_data2 = ["R2", "R2", "R2"]
test_data3 = ["R5", "L5", "R5", "R3", "R3", "R5"]
direction = 0
distance = 0

# open file
f = open("input.txt", "r")

# read file
input = f.read()

# split input into array
input = input.split(", ")

for x in input:
    print("Direction: ", x[0][0], x[1][0])
    if x[0][0] == "R":
        direction += 1
    else:
        direction -= 1

    print (direction)
    if direction > 3 or direction < -3:
        direction = 0

    print (int(x[1:]))
    if 1 >= direction >= -1:
        distance += int(x[1:])
    else:
        distance -= int(x[1:])

    print("Total distance: ", distance)
