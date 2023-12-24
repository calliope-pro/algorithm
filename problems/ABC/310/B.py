# ABC310-B
# setとitertools.permutationsを使うと簡単に解ける
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
items = []
for _ in range(n):
    p, c, *f = rm()
    items.append((p, set(f)))

for (item_i, item_j) in itertools.permutations(items, 2):
    if item_i[0] >= item_j[0] and item_i[1] <= item_j[1] and ((len(item_j[1])>len(item_i[1])) or item_i[0] > item_j[0]):
        print('Yes')
        exit()
print('No')
