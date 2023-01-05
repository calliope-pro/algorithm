# 典型90-055
# PyPy only
# reduceで積計算するのは遅いらしい
# 1つ1つの数は小さいほど掛け算はスピードが速い
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, p, q = rm()
al = rl()
cnt = 0
for co in itertools.combinations(al, r=5):
    prod = co[0]%p * co[1]%p * co[2]%p * co[3]%p * co[4]%p
    if prod % p == q:
        cnt += 1
print(cnt)
