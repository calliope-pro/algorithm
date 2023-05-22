# ABC302-C
# 制約がどちゃくそ小さい -> 脳死で全探索
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
sl = [rr() for _ in range(n)]
for co in itertools.permutations(sl):
    for i in range(n-1):
        cnt = 0
        for c0, c1 in zip(co[i], co[i+1]):
            cnt += (c0 != c1)
            if cnt > 1:
                break
        if cnt > 1:
            break
    else:
        print('Yes')
        exit()
print('No')
