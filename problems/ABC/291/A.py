# ABC291-A
# 大文字があったら何番目かを出力してexit
import sys
from string import ascii_uppercase

rr = lambda: sys.stdin.readline().rstrip()
au = ascii_uppercase

s = rr()
for i, c in enumerate(s, 1):
    if c in au:
        print(i)
        exit()
