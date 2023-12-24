# ABC324-A
# 脳死でsetを使う
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = set(rl())
if len(al) == 1:
    print('Yes')
else:
    print('No')
