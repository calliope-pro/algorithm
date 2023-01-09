# ABC278-C
# n人のデータを保持するのは多すぎて出来ない
# q個のデータしかない -> ハッシュ関連 -> ここでは辞書ベースで実装
# 想定解: タプル(A, B)を集合で管理
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
users = dict()
for _ in range(q):
    t, a, b = rm()
    if t == 1:
        users[a-1] = users.get(a-1, set())
        users[a-1].add(b-1)
    if t == 2:
        users[a-1] = users.get(a-1, set())
        users[a-1].discard(b-1)
    if t == 3:
        if b-1 in users.get(a-1, set()) and a-1 in users.get(b-1, set()):
            print('Yes')
        else:
            print('No')


