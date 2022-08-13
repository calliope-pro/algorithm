# AGC040-A
# RLEを行う。規則を見つける。
# 2>1>0, 4>1>0, 0<1<5のようにしかならない
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
rle = [(key, len(list(li))) for key, li in itertools.groupby(s)]
ans = 0 if rle[0][0] == '<' else rle[0][1]
for idx in range(len(rle)):
    a, b = rle[idx], rle[min(idx + 1, len(rle)-1)]
    if a[0] == '<':
        ans += ((a[1] - 1) * a[1]) // 2
        ans += max(a[1], b[1])
    else:
        ans += ((a[1] - 1) * a[1]) // 2
print(ans)
