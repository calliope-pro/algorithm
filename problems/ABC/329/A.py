# ABC329 - A
# 文字列はiterableなので、joinでスペース区切りにするだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
print(' '.join(s))
