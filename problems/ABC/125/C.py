# ABC125-C
# Python only (オーバーフローの関係かな)
# セグ木でNlogNになるから脳死で貼ったら通った
import sys
import math
from typing import cast, List, Protocol

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

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

n = ri()
al = rl()
st = SegmentTree(al, monoid=al[-1]*al[0], operator=math.gcd)  # monoidは0でもいい
ans = 1
for i in range(n):
    st.update(i, al[i-1])
    ans = max(st.eval(0, n), ans)
    st.update(i, al[i])
print(ans)
