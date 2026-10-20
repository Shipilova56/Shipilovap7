from itertools import combinations
s = input()
a = [int(x) for x in s.split()]
t = 9
r = []
for k in range(1, len(a) + 1):
    for c in combinations(a,k):
        if sum(c) == t:
            v = tuple(sorted(c))
            if v not in r:
                r.append(v)
print(r)