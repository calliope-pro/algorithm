# ABC347-A
# 内包表記+unpack使うと楽
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
print(*sorted(av//k for av in al if av % k == 0))
