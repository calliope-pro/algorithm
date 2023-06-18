# ABC306-C
# 個数をメモしてソート。heapしたけど
import sys
import heapq

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
cnt = [0] * n
ans = []
for i, av in enumerate(al):
    if cnt[av-1] == 0:
        cnt[av-1] += 1
        continue
    if cnt[av-1] == 1:
        cnt[av-1] += 1
        heapq.heappush(ans, (i, av))
        continue
print(' '.join(str(av) for _, av in ans))
