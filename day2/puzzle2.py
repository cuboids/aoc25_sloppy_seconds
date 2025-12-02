import textwrap


f = open('day2/input.txt', 'r')
lines = f.read().split('\n')


silly = []


EXAMPLE = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862",
    "565653-565659",
    "824824821-824824827",
    "2121212118-2121212124",
]


for l in lines:  # or: `for l in EXAMPLE`
    for ll in l.split(","):
        minr, maxr = ll.split("-")
        for i in range(int(minr), int(maxr) + 1):
            str_i = str(i)
            str_len = len(str_i)
            for j in range(1, str_len // 2 + 1):
                if len(set((textwrap.wrap(str_i, j)))) == 1:
                    silly.append(i)
                
print(silly)
print(sum(set(silly)))