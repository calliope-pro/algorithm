# ABC263-C
# itertools.combinationsを使うだけ
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
for com in itertools.combinations(range(1, m+1), n):
    print(*com)
