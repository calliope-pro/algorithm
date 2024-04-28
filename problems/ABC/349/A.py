# ABC349-A
# sumが0になるから、-sumを出力すればいい
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
print(-sum(al))
