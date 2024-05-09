# ABC352-B
# 文字列tの中からsの文字を順番に探していく問題
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
si = 0
for ti, tv in enumerate(t):
    if tv == s[si]:
        si += 1
        print(ti+1, end=" ")
    
