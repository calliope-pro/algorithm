# ABC307-D
# Python only、なぜ？いらいら
# 昔例題あった気がする、(で始まるグループを管理する
import sys
from collections import deque

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
ans = ''
stack = deque([])
for c in s:
    if c == '(':
        stack.append('(')
        continue
    if c == ')':
        if len(stack):
            stack.pop()
        else:
            ans += ')'
        continue
    if len(stack):
        stack[-1] += c
    else:
        ans += c
print(f"{ans}{''.join(stack)}")
