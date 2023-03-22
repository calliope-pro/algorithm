# ABC291-B
# Pythonのスライスで中間3n区間を取得するだけ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
xl = rl()
xl.sort()
print(sum(xl[n:-n]) / (3*n))
