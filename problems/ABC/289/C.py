# ABC289-C
# 制約は小さいので全探索でいい
# Pythonなので、itertools.combinationsを使えば脳死で組み合わせを取得できる
import sys
import itertools

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
sets = []
for _ in range(m):
    ri()
    sets.append(set(rl()))
ans = 0
for i in range(1, m+1):
    for sc in itertools.combinations(sets, r=i):
        set_ = set()
        for sc_set in sc:
            set_.update(sc_set)
        if len(set_) == n:
            ans += 1
print(ans)

