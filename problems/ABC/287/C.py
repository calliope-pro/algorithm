# ABC287-C
# 閉路がないパスになるグラフをパスグラフというらしい
# 次数をUnion-Findに付け加えた(1-2, 1-3, 1-4に対応するため)
import sys

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
    dim_ = None # 次数

    def __init__(self, n=6*10**5+3):
        '''
        Parameters
        ----------
        n: int, default 6*10**5+3
            number of nodes
        '''
        self.par_ = list(range(n))
        self.rank_ = [0] * n
        self.dim_ = [0] * n

    def root(self, x):
        if x == self.par_[x]:
            return x
        return self.root(self.par_[x])

    def rank(self, x):
        return self.rank_[x]

    def dim(self, x):
        return self.dim_[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        self.dim_[x] += 1
        self.dim_[y] += 1
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
if m != n-1:
    print('No')
    exit()
uf = UnionFind(n)
for _ in range(m):
    u, v = rm()
    u -= 1
    v -= 1
    if uf.is_same(u, v):
        print('No')
        exit()
    uf.union(u, v)
    if uf.dim(u) > 2 or uf.dim(v) > 2:
        print('No')
        exit()
print('Yes')
