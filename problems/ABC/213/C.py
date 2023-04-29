# ABC213-C
# それぞれが独立な座圧なので、2回座圧を行うだけ。
import sys

rm = lambda: map(int, sys.stdin.readline().split())

h, w, n = rm()
a_set = set()
b_set = set()
ab = []
for _ in range(n):
    a, b = rm()
    a_set.add(a)
    b_set.add(b)
    ab.append((a, b))
c_a = {v:i for i, v in enumerate(sorted(a_set), 1)}
c_b = {v:i for i, v in enumerate(sorted(b_set), 1)}
for (a, b) in ab:
    print(c_a[a], c_b[b])
