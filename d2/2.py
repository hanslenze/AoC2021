# f = (open("example.txt", "r")).readlines()
f = (open("input.txt", "r")).readlines()
f = [g.strip() for g in f]

hor = 0
dep = 0
aim = 0

for i in f:
    if 'forward' in i:
        hor = hor + int(i.split()[1])
        dep = dep + (aim * int(i.split()[1]))
    if 'down' in i:
        aim = aim + int(i.split()[1])
    if 'up' in i:
        aim = aim - int(i.split()[1])

b = hor * dep
print(b)