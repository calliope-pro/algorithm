# ABC291-C
# 問題文とサンプルがひっかけに来ようとしてる
# 集合で管理 + ループしっかり実装すれば問題ない
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
passed = set()
x = 0
y = 0
passed.add((x, y))
for c in s:
    if c == 'L':
        x -= 1
    elif c == 'R':
        x += 1
    elif c == 'U':
        y += 1
    else:
        y -= 1
    if (x, y) in passed:
        print('Yes')
        exit()
    passed.add((x, y))
print('No')

