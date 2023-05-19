# ABC297-E
# 感動した。
# k番目は0円含んでk+1番目と読み替える
# 小さい値(t+1) = 小さい値(1~t) + avなので、候補を全て入れていけばいい。
# 小さい順に候補を入れてく。小さい順に取り出す。被りと個数は管理する。
import sys
import heapq

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n, k = rm()
al = rl()
h = [0]
last = -inf
cnt = -1
while cnt < k:
    min_ = heapq.heappop(h)
    if min_ > last:
        last = min_
        cnt += 1
        for av in al:
            heapq.heappush(h, av + min_)
print(last)
