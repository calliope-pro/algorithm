# PAST006-E
# 制約が小さめなので、dequeでの削除も高々3なので、dequeで挿入コスト減らすだけでいける
import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

a = collections.deque()
n = ri()
s = rr()
for i, c in enumerate(s, 1):
    if c == 'L':
        a.appendleft(i)
    elif c == 'R':
        a.append(i)
    elif c == 'A':
        if len(a) <= 0:
            print('ERROR')
        else:
            print(a.popleft())
    elif c == 'B':
        if len(a) <= 1:
            print('ERROR')
        else:
            print(a[1])
            del a[1]
    elif c == 'C':
        if len(a) <= 2:
            print('ERROR')
        else:
            print(a[2])
            del a[2]
    elif c == 'D':
        if len(a) <= 0:
            print('ERROR')
        else:
            print(a.pop())
    elif c == 'E':
        if len(a) <= 1:
            print('ERROR')
        else:
            print(a[-2])
            del a[-2]
    elif c == 'F':
        if len(a) <= 2:
            print('ERROR')
        else:
            print(a[-3])
            del a[-3]



