# ABC293-A
# 交互に出力されればいい
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
for a, b in zip(s[1::2], s[::2]):
    print(f'{a}{b}', end="")
