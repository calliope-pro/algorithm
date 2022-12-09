# ABC280-C
# 文字数の長い方に合わせるためにitertools.zip_longestを使う必要あり
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
for i, (s_, t_) in enumerate(itertools.zip_longest(s, t)):
    if s_ != t_:
        print(i+1)
        break
