# ARC006-C
# 貪欲法
import sys
ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()

li = [inf]

for _ in range(n):
    w = ri()
    for i in range(len(li)):
        if w <= li[i]:
            li[i] = w
            break
    else:
        li.append(w)
print(len(li))

