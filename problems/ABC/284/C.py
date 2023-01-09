# ABC284-C
# UnionFind使うと楽, (想定解はDFSによる探索+探索済みかどうかのリストとの組み合わせ)
# unionメソッドは既にunionされたノードの根は更新しない -> 最後にループでrootメソッドを使って確かめる
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
uf = UnionFind(n)
for _ in range(m):
    u, v = rm()
    uf.union(u-1, v-1)

ans = 0
for i in range(n):
    ans += i==uf.root(i)
print(ans)
print(uf.par_)