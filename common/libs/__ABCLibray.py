import math
from typing import List, Sequence, Optional

def rotate90(m: Sequence[Sequence]) -> List[tuple]:
    '''
    二次元の配列やシーケンスを右に90度回転

    Parameters
    ----------
    m : Sequence[Sequence]
        回転させたい二次元配列およびそれに近しいシーケンス

    Returns
    -------
    List[tuple]
        回転後の行列
    '''
    return list(zip(*m[::-1]))

class GeometryHandler:
    @classmethod
    def calc_triangle_area(cls, x0, y0, x1, y1, x2, y2) -> int:
        '''
        3点より三角形の面積を算出

        Parameters
        ----------
        x0, y0 : int
            点(x0, y0)となる
        x1, y1 : int
            点(x1, y1)となる
        x2, y2 : int
            点(x2, y2)となる

        Returns
        -------
        int
            三角形の面積
        '''
        area = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
        area = 1/2 * abs(area)
        return area

    @classmethod
    def is_convex(cls, x0, y0, x1, y1) -> bool:
        '''
        隣接する2辺に関する凸性判定

        Parameters
        ----------
        x0, y0 : int
            0度の基準となる辺・ベクトル
            (x0, y0)となる辺・ベクトル
        x1, y1 : int
            (x1, y1)となる辺・ベクトル

        Returns
        -------
        bool
            凸性の有無
            (x0, y0)から反時計回りに180度以上ならば凸性が認められずFalse
        '''
        return (x0*y1 - x1*y0) > 0

class PrimeHandler:
    @classmethod
    def get_prime_list(cls, n: int) -> List[int]:
        '''
        エラトステネスの篩を用いた素数列挙

        Parameters
        ----------
        n : int
            最大値

        Returns
        -------
        List[int]
            2 ~ nにおける素数リスト

        Raises
        ------
        AssertionError
            `n`が0以下の場合
        '''
        assert n >= 1, '`n` must be 1 or more.'
        prime_list = []
        is_prime_list = [True] * (n+1)
        is_prime_list[0] = False
        is_prime_list[1] = False
        for i in range(2, n+1):
            if is_prime_list[i]:
                prime_list.append(i)
                for j in range(i, n+1, i):
                    is_prime_list[j] = False
        return prime_list
    
    @classmethod
    def prime_factorization(cls, n: int, *, is_decoded: bool=False, ps: Optional[List[int]]=None) -> List[int]:
        '''
        素因数分解し、素因数列挙

        Parameters
        ----------
        n : int
            素因数分解する数
        is_decoded : bool, optional
            展開するか, by default False
        ps : List[int] | None, optional
            事前に準備された素数のリスト

        Returns
        -------
        List[int]
            素因数のリスト
            展開している場合は各々の素因数の個数入っている
        '''
        prime_list = []
        if ps is None:
            ps = cls.get_prime_list(math.ceil(n**0.5) + 1)
        for psv in ps:
            if n % psv != 0:
                continue
            while n % psv == 0:
                n //= psv
                if is_decoded:
                    prime_list.append(psv)
            if not is_decoded:
                prime_list.append(psv)
        else:
            if n != 1:
                prime_list.append(n)
        return prime_list

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

class SegTree:
    from operator import add
    '''SegmentTree
    
    Attributes
    ----------
    nodes: list of int or float
    monoid: int or float
        単位元, Monoid
    nodes_length: int
        objectの長さ以上の最小の2^k-1
        The smallest 2^k-1 over the length of object
    seg_func: function
    '''
    nodes = None
    monoid = None
    nodes_length = None
    seg_func = None

    def __init__(self, object, *, monoid=0, seg_func=add):
        '''
        Parameters
        ----------
        object: array_like
            
        monoid: int or float default 0
            単位元, Monoid
        seg_func: function default operator.add
            セグ木にて用いる関数
            Function used in SegTree
        '''
        bin_n = bin(len(object))[2:]
        sum_bin_n = sum(int(i) for i in bin_n)
        if sum_bin_n == 1:
            cnt_nodes = 2**(len(bin_n) - 1)
        else:
            cnt_nodes = 2**len(bin_n)

        self.monoid = monoid
        self.nodes_length = 2*cnt_nodes - 1
        self.seg_func = seg_func
        self.nodes = [monoid] * (2*cnt_nodes - 1)
        
        for i, v in enumerate(object):
            self.update(i, v)
            self.eval(i)

    def get_node_idx(self, node):
        '''get node_idx in SegTree
        Parameters
        ----------
        node: int
            objectにおけるnodeのインデックス
            Index of node in object
        Returns
        -------
        node_idx: int
            node_idx in SegTree
        '''
        node_idx = self.nodes_length//2 + node
        return node_idx
    
    def update(self, node, val):
        '''
        Parameters
        ----------
        node: int
            objectにおけるnodeのインデックス
            Index of node in object
        val: int or float
            変えたい値
            Value to replace
        '''
        node_idx = self.get_node_idx(node)
        self.nodes[node_idx] = val

    def eval(self, node):
        '''
        Parameters
        ----------
        node: int
            objectにおけるnodeのインデックス
            Index of node in object
        '''
        node_idx = self.get_node_idx(node)
        while node_idx > 0:
            node_idx = math.ceil(node_idx/2) - 1
            self.nodes[node_idx] = self.seg_func(
                self.nodes[node_idx*2 + 1],
                self.nodes[node_idx*2 + 2]
            )

    def _get(self, query_left, query_right, _node_idx=0, _layer_left=0, _depth=1):
        '''
        Notes
        -----
        Don't change _node_idx, _layer_left, _depth
        '''
        cnt_layer_nodes = (self.nodes_length + 1) // (2**_depth)
        layer_right = _layer_left + cnt_layer_nodes - 1

        if _layer_left > query_right or layer_right < query_left:
            return self.monoid
        
        elif _layer_left >= query_left and layer_right <= query_right:
            return self.nodes[_node_idx]
        
        else:
            val_left = self._get(query_left, query_right, _node_idx*2+1, _layer_left, _depth+1)
            val_right = self._get(query_left, query_right, _node_idx*2+2, _layer_left + cnt_layer_nodes//2, _depth+1)
            return self.seg_func(val_right, val_left)
    
    def get(self, query_left, query_right):
        '''
        Returns
        -------
        self._get(query_left, query_right): int or float
            閉区間[query_left, query_right]の値
            Value of closed section[query_left, query_right]
        '''
        if query_right == -1:
            query_right = (self.nodes_length + 1) // 2
        return self._get(query_left, query_right)
