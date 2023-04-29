# ABC300-C
# 問題が親切なので、左上から右下までの1直線の長さが3以上のものを調べればいい
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
cm = [rr() for _ in range(h)]
passed = [[0]*w for _ in range(h)]
ans = [0] * min(h, w)
for i in range(h):
    for j in range(w):
        if cm[i][j] == '#' and passed[i][j] == 0:
            len_ = 0
            passed[i][j] = 1
            for dx in range(104):
                if 0 <= i+dx < h and 0 <= j+dx < w and cm[i+dx][j+dx] == '#':
                    passed[i+dx][j+dx] = 1
                    len_ += 1
                else:
                    break
            if len_ > 2:
                ans[len_//2 - 1] += 1
print(*ans)
