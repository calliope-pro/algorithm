# ABC285-B
# 文章読みにくいねん
# 普通に二重ループとスライス記法の組み合わせ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
for i in range(1, n):
    for idx, (s1, s2) in enumerate(zip(s, s[i:])):
        if s1 == s2:
            print(idx)
            break
    else:
        print(idx+1)
