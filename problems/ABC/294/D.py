# ABC294-D
# データ構造はプライオリキューと集合で管理する
# 最後の結果が広義単調増加になるため、rangeの下限を管理していくと線形時間で終わる
# sortedsetがあればsetから最小値を取得するにも最適化されるが。。。
import sys
import heapq

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
not_called = list(range(1, n+1))
called = set()
gone = set()
ans = 1
heapq.heapify(not_called)
for _ in range(q):
    event = rl()
    i = event[0]
    if i == 1:
        min_ = heapq.heappop(not_called)
        called.add(min_)
    elif i == 2:
        x = event[1]
        called.remove(x)
        gone.add(x)
    else:
        for i in range(ans, n+1):
            if i not in gone and i in called:
                ans = i
                print(i)
                break
