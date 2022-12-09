# ABC272-B
# 制約緩いので、集合を用いて組み合わせの総数が正しいか検査した
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
s = set()
for _ in range(m):
    k, *x = rm()
    s.update(itertools.combinations(x, r=2))
print('Yes' if len(s) == n*(n-1)//2 else 'No')
