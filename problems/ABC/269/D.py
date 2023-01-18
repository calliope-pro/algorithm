# ABC269-D
# 制約が小さいので、全部に対して探索が可能だと考える
# ある任意の点から探索可能なだけ探索 -> 探索出来る点は集合から削除 -> 探索できない -> 1グループ
import sys
import queue

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
set_ = set()
for _ in range(n):
    x, y = rm()
    set_.add((x-1, y-1))

cnt = 0
while len(set_):
    point = set_.pop()
    q = queue.Queue()
    q.put(point)
    while q.qsize():
        x, y = q.get()
        if (x-1, y-1) in set_:
            q.put((x-1, y-1))
            set_.discard((x-1, y-1))
        if (x-1, y) in set_:
            q.put((x-1, y))
            set_.discard((x-1, y))
        if (x, y-1) in set_:
            q.put((x, y-1))
            set_.discard((x, y-1))
        if (x, y+1) in set_:
            q.put((x, y+1))
            set_.discard((x, y+1))
        if (x+1, y) in set_:
            q.put((x+1, y))
            set_.discard((x+1, y))
        if (x+1, y+1) in set_:
            q.put((x+1, y+1))
            set_.discard((x+1, y+1))
    cnt += 1
print(cnt)
