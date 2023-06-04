# ABC304-C
# CでUnion-Findか。。。インフレおかしすぎて
# 1とルートが同じかどうかを考える。BFSとかでもいいけど
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

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

n, d = rm()
uf = UnionFind(n+10)
xy = [rl() for _ in range(n)]
for idx, (x, y) in enumerate(xy[1:], 1):
    for idx_, (x_, y_) in enumerate(xy[:idx]):
        if (x-x_)**2 + (y-y_)**2 <= d**2:
            uf.union(idx, idx_)
root_0 = uf.root(0)
for i in range(n):
    if root_0 == uf.root(i):
        print('Yes')
    else:
        print('No')
