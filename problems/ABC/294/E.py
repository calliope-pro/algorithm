# ABC294-E
# 2重ループにする必要はない。上のリストにおけるインデックス間での下のリストの候補が対応するかを実装すればいい
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

l, n1, n2 = rm()
v1 = [rl() for _ in range(n1)]
v2 = collections.deque([rl() for _ in range(n2)])
ans = 0
left = 0
left_ = 0
for v, cnt in v1:
    right = left + cnt
    while len(v2):
        v_, cnt_ = v2.popleft()
        right_ = left_ + cnt_
        if right < right_:
            tmp = right - max(left, left_)
            if v == v_:
                ans += tmp
            v2.appendleft([v_, cnt_-tmp])
            left_ = right
            left = right
            break
        else:
            if v == v_:
                ans += (right_ - max(left, left_))
            left_ = right_
print(ans)

