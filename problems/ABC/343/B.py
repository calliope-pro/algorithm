# ABC343-B
# 1が立っている場所を出力するだけ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
for _ in range(n):
    al = rl()
    for i, av in enumerate(al, 1):
        if av == 1:
            print(i, end=" ")
    print()
