# ABC351-B
# めんどくさかったのでnumpyで異なる箇所のインデックスを取得した
import numpy as np
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
ri = lambda: int(sys.stdin.readline())

n = ri()
am = np.array([rsl() for _ in range(n)])
bm = np.array([rsl() for _ in range(n)])
print(*(np.argwhere(am != bm)+1)[0])
