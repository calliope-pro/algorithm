# ABC322-B
# メソッドを使う + スコア計算を簡略化
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
s = rr()
t = rr()
print((not t.startswith(s))*2 + (not t.endswith(s)))
