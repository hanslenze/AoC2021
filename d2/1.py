# f = (open("example.txt", "r")).readlines()
f = (open("input.txt", "r")).readlines()
f = [g.strip() for g in f]

x = 0
y = 0

for i in f:
    if 'forward' in i:
        x = x + int(i.split()[1])
    if 'down' in i:
        y = y + int(i.split()[1])
    if 'up' in i:
        y = y - int(i.split()[1])

a = x * y
print(a)