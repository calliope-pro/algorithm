import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
li = []
li_ = [None] * m
counter = collections.Counter()
for idx in range(m):
    p, y = rm()
    li.append([y, p, idx])
li.sort()
for v in li:
    idx = v[2]
    p = v[1]
    counter[p] += 1
    li_[idx] = f'{str(p).zfill(6)}{str(counter[p]).zfill(6)}'
print(*li_, sep='\n')

