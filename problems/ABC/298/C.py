# ABC298-C
# 昇順なので、とりあえずheapqを使えばなんとかなる(bisect使ってもいいね)
# そこまで制約厳しいわけじゃ無いので、集合の方は適当にsorted使った
import sys
import collections
import heapq

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
q = ri()
c = collections.defaultdict(list)
h = collections.defaultdict(set)
for _ in range(q):
    flag, *query = rm()
    if flag == 1:
        i = query[0]
        j = query[1]
        heapq.heappush(c[j], i)
        h[i].add(j)
    elif flag == 2:
        i = query[0]
        print(*heapq.nsmallest(len(c[i]), c[i]))
    else:
        i = query[0]
        print(*sorted(h[i]))

