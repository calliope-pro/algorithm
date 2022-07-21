# ABC206-D
# UnionFind
import sys
ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

class UnionFind():
    _par = None
    _rank = None

    def __init__(self, n):
        self._par = list(range(n))
        self._rank = [0] * n

    def get_root(self, x):
        if x == self._par[x]:
            return x
        return self.get_root(self._par[x])

    def get_rank(self, x):
        return self._rank[x]

    def is_same(self, x, y):
        return self.get_root(x) == self.get_root(y)

    def union(self, x, y):
        x = self.get_root(x)
        y = self.get_root(y)
        rank_x = self.get_rank(x)
        rank_y = self.get_rank(y)
        if x != y:
            if rank_x == rank_y:
                self._rank[x] += 1
                self._par[y] = x
            elif rank_x > rank_y:
                self._par[y] = x
            else:
                self._par[x] = y

n = ri()
a = rl()
b = reversed(a)
union_find = UnionFind(2*10**5+10)
ans = 0
for aa, bb in zip(a, b):
    if aa != bb:
        if not union_find.is_same(aa, bb):
            ans += 1
        union_find.union(aa, bb)

print(ans)











