import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, w = rm()
a = rl()
d = set()
for r in range(1, 4):
    for combination in itertools.combinations(a, r):
        if (sum_:=sum(combination)) <= w:
            d.add(sum_)
print(len(d))
