# ABC268-C
# N^2にしないようにする必要がある
# pvが人を喜ばすために何回転する必要があるかをrotate_cntsに持たせる
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
pl = rl()
rotate_cnts = [0] * n
for i, pv in enumerate(pl):
    rotate_cnts[(pv-i-1) % n] += 1
    rotate_cnts[(pv-i) % n] += 1
    rotate_cnts[(pv-i+1) % n] += 1
print(max(rotate_cnts))
