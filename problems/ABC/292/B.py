# ABC292-B
# ループと、カウントの変数を保持すればいい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
counts = [0] * n
for _ in range(q):
    event_id, x = rm()
    if event_id == 1:
        counts[x-1] += 1
    if event_id == 2:
        counts[x-1] += 2
    if event_id == 3:
        if counts[x-1] >= 2:
            print('Yes')
        else:
            print('No')

