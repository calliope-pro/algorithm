# PAST005-D
# itertools.takewhileで左からTrueのものの個数が取得できる
# あとはタプルを使って単に複数キーでソートする
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
li = []
for _ in range(n):
    s = rr()
    li.append((int(s), -len(list(itertools.takewhile(lambda x: x=='0', s))), s))
li.sort()
for _, _, v in li:
    print(v)
