# ABC264-D
# 転倒数使うらしいが知らん
# 'a'が0番目になる回数 + 'a'がない状況で't'が1番目になる回数をシミュレートしただけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
cnt = 0
atcoder = 'atcoder'
while True:
    if len(s) == 0:
        print(cnt)
        break
    j = s.index(atcoder[0])
    atcoder = atcoder[1:]
    cnt += j
    s = s[:j] + s[j+1:]
