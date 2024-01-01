# ABC325-B
# 標準時刻で参加できる最大値を求める
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
l = [0] * 24
for _ in range(n):
    w, x = rm()
    for i in range(9, 18):
        l[(i+x) % 24] += w
print(max(l))
