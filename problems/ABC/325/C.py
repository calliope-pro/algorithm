# ABC325-C
# UnionFindで連結成分を求めた後、根の数を数える
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())


class UnionFind:
    """UnionFind

    Attributes
    ----------
    par_: list of int
        ノードの根
        parent of node
    rank_: list of int
        ノードのランク、長さ
        rank of node
    """

    par_ = None
    rank_ = None

    def __init__(self, n=6 * 10**5 + 3):
        """
        Parameters
        ----------
        n: int, default 6*10**5+3
            number of nodes
        """
        self.par_ = list(range(n))
        self.rank_ = [0] * n

    def root(self, x):
        if x == self.par_[x]:
            return x
        return self.root(self.par_[x])

    def rank(self, x):
        return self.rank_[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        rank_x = self.rank(x)
        rank_y = self.rank(y)
        if x != y:
            if rank_x == rank_y:
                self.rank_[x] += 1
                self.par_[y] = x
            elif rank_x > rank_y:
                self.par_[y] = x
            else:
                self.par_[x] = y


h, w = rm()
sm = [rsl() for _ in range(h)]
uf = UnionFind(h * w)
cnt = 0
for i in range(h):
    for j in range(w):
        if sm[i][j] == "#":
            sm[i][j] = cnt
            for di, dj in [
                # (1, 0),
                (-1, 0),
                # (0, 1),
                (0, -1),
                # (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ]:
                if 0 <= i + di < h and 0 <= j + dj < w:
                    if sm[i + di][j + dj] not in {".", "#"}:
                        uf.union(cnt, sm[i + di][j + dj])
            cnt += 1

print(len(set(uf.root(par_) for par_ in set(uf.par_[:cnt]))))
