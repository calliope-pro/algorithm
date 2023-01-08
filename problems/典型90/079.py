# 典型90-079
# それぞれの行列の要素の差を調べて、制約が小さいため2重ループでシミュレーションする
# numpyのファンシーインデックス使うと楽に書ける
import sys
import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

h, w = rm()
am = np.array([rl() for _ in range(h)])
bm = np.array([rl() for _ in range(h)])
cm = am - bm
ans = 0
for i in range(w-1):
    for j in range(h-1):
        ans += abs(cm[j][i])
        cm[j:j+2, i:i+2] -= cm[j][i]
if cm.sum() == 0:
    print('Yes')
    print(ans)
else:
    print('No')
