# ABC326-B
# n以上で、数値<->文字列変換してチェックするだけ
import sys

ri = lambda: int(sys.stdin.readline())

n_ = ri()
for i in range(n_, 1000):
    n = str(i)
    if int(n[0]) * int(n[1]) == int(n[2]):
        print(i)
        exit()
