# ABC225-D
# nの制約や出力数に制限が設けられている -> 単純なデータ管理方法を考える
# 連結・分離 -> 前後の関係が変わる -> 前後に関するデータを持っておけばいい
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
prev_train = [None] * (n + 1)
next_train = [None] * (n + 1)
for _ in range(q):
    query = rl()
    if query[0] == 1:
        x, y = query[1], query[2]
        prev_train[y] = x
        next_train[x] = y
    if query[0] == 2:
        x, y = query[1], query[2]
        prev_train[y] = None
        next_train[x] = None
    if query[0] == 3:
        x = query[1]
        li = collections.deque()
        while True:
            if prev_train[x] is None:
                break
            li.appendleft(prev_train[x])
            x = prev_train[x]
        x = query[1]
        li.append(x)
        while True:
            if next_train[x] is None:
                break
            li.append(next_train[x])
            x = next_train[x]
        print(len(li), *li)
