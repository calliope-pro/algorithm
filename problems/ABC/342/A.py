# ABC342-A
# それぞれの出現頻度をカウントして、1回しか出現しないものの場所を出力する
import collections
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
c = collections.Counter(s)
for k, v in c.items():
    if v == 1:
        print(s.index(k) + 1)
