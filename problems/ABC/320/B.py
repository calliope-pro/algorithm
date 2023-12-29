# ABC320-B
# 1文字ずつ減らしていって、回文になるかどうかを調べる。
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
for i in range(len(s), 0, -1):
    for j in range(len(s) - i + 1):
        s_ = s[j:j + i]
        if s_ == s_[::-1]:
            print(i)
            exit()