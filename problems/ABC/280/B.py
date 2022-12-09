# ABC280-B
# numpy使ってそれぞれの要素間差分を楽に計算
import sys
import numpy as np

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
s = np.array(rl())
print(s[0], *(s[1:]-s[:-1]))
