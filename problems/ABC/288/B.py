# ABC288-B
# pythonは文字もソートできる
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
sl = [rr() for _ in range(n)]
print(*sorted(sl[:k]), sep='\n')
