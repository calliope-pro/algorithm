import sys
import itertools

ri = lambda: int(sys.stdin.readline())

n = ri()
cnt = 0
for l in range(3, len(str(n))+1):
    for co in itertools.product((3, 5, 7), repeat=l):
        if len(set(co)) != 3:
            continue
        s = 0
        for c in co:
            s = s*10 + c
        if s <= n:
            cnt += 1
print(cnt)
