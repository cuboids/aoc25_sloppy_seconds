import re


f = open('day3/input.txt', 'r')
lines = f.read().split('\n')


joltage = []


EXAMPLE = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",

]


for bank in lines:

    for i in range(100, 9, -1):
        pattern = rf".*{str(i)[0]}.*{str(i)[1]}.*"
        if re.match(pattern, bank):
            joltage.append(i)
            break


print(sum(joltage))