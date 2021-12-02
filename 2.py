#f = (open("example.txt", "r")).readlines()
f = (open("input.txt", "r")).readlines()
f = [g.strip() for g in f]
c = 0
n = len(f)

for i in range(2, n):
    if (int(f[i]) + int(f[i-1]) + int(f[i-2])) - ((int(f[i-1]) + int(f[i-2]) + int(f[i-3]))) > 0:
        c += 1

c