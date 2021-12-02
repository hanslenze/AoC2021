#f = (open("example.txt", "r")).readlines()
f = (open("input.txt", "r")).readlines()
f = [int(g.strip()) for g in f]
c = 0
n = len(f)

for i in range(2, n):
    if (f[i] + f[i-1] + f[i-2]) - ((f[i-1] + f[i-2] + f[i-3])) > 0:
        c += 1

c