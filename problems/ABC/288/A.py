# ABC288-A
# 単純にループとsum関数
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
for _ in range(n):
    print(sum(rl()))
