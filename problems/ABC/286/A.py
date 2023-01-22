# ABC286-A
# pythonだとリストのままswapできるから嬉しいね
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, p, q, r, s = rm()
al = rl()
al[p-1:q], al[r-1:s] = al[r-1:s], al[p-1:q]
print(*al)
