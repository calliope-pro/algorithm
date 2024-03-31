# ABC346-A
# zipとunpackを駆使すると楽
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
print(*(a * b for a, b in zip(al, al[1:])))
