import math
from typing import cast, List, Sequence, Optional, Protocol

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

class Operator(Protocol):
    def __call__(self, *args: int) -> int:
        ...

class SegmentTree:
    '''
    セグメントツリー

    Attributes
    ----------
    tree : List[int]
        セグメントツリーの木構造配列
    monoid : int
        単位元
    operator : Operator
        評価関数
    '''
    tree: List[int]
    monoid: int
    operator: Operator

    def __init__(
        self,
        base_array: List[int],
        *,
        monoid: int = cast(int, float("inf")),
        operator: Operator = min
    ) -> None:
        '''
        セグメントツリーインスタンス生成

        Parameters
        ----------
        base_array : List[int]
            元となる配列
        monoid : int, optional
            単位元, by default cast(int, float("inf"))
        operator : Operator, optional
            評価関数, by default min
        '''
        self.monoid = monoid
        self.operator = operator
        base_array_length = len(base_array)
        segment_tree_length = 2 ** (math.ceil(math.log2(base_array_length)) + 1) - 1
        self.tree = (
            [monoid] * (segment_tree_length // 2)
            + [*base_array]
            + [monoid] * ((segment_tree_length + 1) // 2 - base_array_length)
        )
        for i in range(segment_tree_length // 2 - 1, -1, -1):
            left_child_idx = i * 2 + 1
            self.tree[i] = self.operator(
                self.tree[left_child_idx], self.tree[left_child_idx + 1]
            )

    def get(self, idx: int) -> int:
        """
        要素を取得

        Parameters
        ----------
        idx : int
            元の配列におけるindex

        Returns
        -------
        int
            指定された要素
        """
        tree_idx = len(self.tree) // 2 + idx
        return self.tree[tree_idx]

    def update(self, idx: int, new_value: int) -> None:
        """
        要素を更新

        Parameters
        ----------
        idx : int
            元の配列におけるindex
        new_value : int
            新たな値
        """
        tree_idx = len(self.tree) // 2 + idx
        self.tree[tree_idx] = new_value
        while tree_idx > 0:
            tree_idx = (tree_idx - 1) // 2
            prev_value = self.tree[tree_idx]
            self.tree[tree_idx] = self.operator(
                self.tree[2 * tree_idx + 1], self.tree[2 * tree_idx + 2]
            )
            if prev_value == self.tree[tree_idx]:
                break

    def eval(self, left_idx: int, right_idx: int) -> int:
        """
        半開区間[left_idx, right_idx)を評価

        Parameters
        ----------
        left_idx : int
            元の配列における左側のindex
        right_idx : int
            元の配列における右側のindex

        Returns
        -------
        int
            評価された値
        """
        return self._eval(left_idx, right_idx)

    def _eval(self, left_idx: int, right_idx: int, *, _l=0, _r=None) -> int:
        '''
        半開区間[left_idx, right_idx)を再帰的評価

        Parameters
        ----------
        left_idx : int
            元の配列における左側のindex
        right_idx : int
            元の配列における右側のindex
        _l : int, optional
            対象となる区間の左側index, by default 0
        _r : int, optional
            対象となる区間の左側index, by default None

        Returns
        -------
        int
            評価された値
        '''
        if _r is None:
            _r = (len(self.tree) + 1) // 2
        if _r <= left_idx or _l >= right_idx:
            return self.monoid
        if left_idx <= _l and _r <= right_idx:
            max_layer = math.log2((len(self.tree) + 1) // 2)
            current_layer = math.log2(_r - _l)
            tree_idx = 2 ** (max_layer - current_layer) - 1 + _r // (_r - _l) - 1
            return self.tree[int(tree_idx)]
        mid = (_l + _r) // 2
        return self.operator(
            self._eval(left_idx, right_idx, _l=_l, _r=mid),
            self._eval(left_idx, right_idx, _l=mid, _r=_r),
        )
