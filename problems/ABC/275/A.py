# ABC275-A
# 最高値のインデックス取得はnp.argmaxが楽
import sys
import numpy as np

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
h = rl()
print(np.argmax(h)+1)
