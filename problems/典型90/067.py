# 典型90-067
# intとnp.base_repr関数でn進法を表現すると楽
import sys
import numpy as np

rs = lambda: sys.stdin.readline().split()

n, k = rs()
k = int(k)
for _ in range(k):
    n = np.base_repr(int(n, base=8), 9).replace(*'85')
print(n)
