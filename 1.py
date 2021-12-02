# f = (open("example.txt", "r")).readlines()
f = (open("input.txt", "r")).readlines()
f = [int(g.strip()) for g in f]
c = 0
n = len(f)

for i in range(1, n):
    if (f[i] - f[i-1] > 0):
        c += 1

c