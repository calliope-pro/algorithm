# PAST011-D
# それぞれの英小文字は取り換え可能 -> グラフではパスが存在する -> UnionFindでパスが存在するか調べるとよい
import sys
from string import ascii_lowercase

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
al = ascii_lowercase

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

uf = UnionFind(len(al))
n = ri()
for _ in range(n):
    a, b = rs()
    uf.union(al.index(a), al.index(b))
s = rr()
t = rr()
for s_, t_ in zip(s, t):
    if not uf.is_same(al.index(s_), al.index(t_)):
        print('No')
        exit()
print('Yes')
