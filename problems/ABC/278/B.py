# ABC278-B
# 繰り上げを条件分岐で計算したいのでwhileにするとすっきり書ける
import sys

rm = lambda: map(int, sys.stdin.readline().split())

h, m = rm()
while True:
    h_str = str(h).zfill(2)
    w_str = str(m).zfill(2)
    if 0 <= int(h_str[0] + w_str[0]) < 24 and 0 <= int(h_str[1] + w_str[1]) < 60:
        print(h, m)
        exit()
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
