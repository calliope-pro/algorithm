# ABC304-E
# Union-Find使う + set使うだけ
# 繋げるべき点のルートがあるかどうか検証するだけ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

class UnionFind:
    '''UnionFind
    
    Attributes
    ----------
    par_: list of int
        ノードの根
        parent of node
    rank_: list of int
        ノードのランク、長さ
        rank of node
    '''
    par_ = None
    rank_ = None

    def __init__(self, n=6*10**5+3):
        '''
        Parameters
        ----------
        n: int, default 6*10**5+3
            number of nodes
        '''
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

n, m = rm()
uf = UnionFind(n+5)
for _ in range(m):
    u, v = rm()
    u -= 1
    v -= 1
    uf.union(u, v)
k = ri()
xy = set()
for _ in range(k):
    x, y = rm()
    x -= 1
    y -= 1
    xy.add((uf.root(x), uf.root(y)))
q_ = ri()
for _ in range(q_):
    p, q = rm()
    p -= 1
    q -= 1
    root_p = uf.root(p)
    root_q = uf.root(q)
    if (root_q, root_p) in xy or (root_p, root_q) in xy:
        print('No')
    else:
        print('Yes')
