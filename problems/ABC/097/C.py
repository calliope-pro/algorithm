# ABC097-C
# kの制約に注目する(k <= 5)
# k番目の文字の長さは高々l=5であることを利用
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

s = rr()
k = ri()
set_ = set()
for l in range(1, min(len(s)+1, 6)):
    for i in range(len(s)-l+1):
        set_.add(s[i:i+l])
print(sorted(set_)[k-1])
