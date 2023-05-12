# ABC230-C
# #の座標と基準点座標の関係を調べる
# あとはindexが対象となるかをループで調べるだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, a, b = rm()
p, q, r, s = rm()
h = q - p + 1
w = s - r + 1
for i in range(h):
    for j in range(w):
        if (p+i) + (r+j) == a+b or a-p-i == b-r-j:
            print('#', end='')
        else:
            print('.', end='')
    print()

