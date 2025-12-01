f = open('day1/input.txt', 'r')
lines = f.read().split('\n')


dial = 50
n_zeroes = 0


EXAMPLE = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


for l in lines:  # or: `for l in EXAMPLE`
    direction = l[0]
    magnitude = int(l[1:])

    if direction.casefold() == "l":
        for m in range(magnitude):
            dial = (dial - 1) % 100
            if not dial:
                n_zeroes +=1

    if direction.casefold() == "r":
        for m in range(magnitude):
            dial = (dial + 1) % 100
            if not dial:
                n_zeroes +=1


print(n_zeroes)