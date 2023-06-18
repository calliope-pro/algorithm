# ABC306-E
# multisetと遷移の条件分岐
# Pythonでmultisetやめちくり
import sys
import heapq

rm = lambda: map(int, sys.stdin.readline().split())

class MultiSet:
    """多重集合

    重複する整数の集合を保持する

    """
    def __init__(self):
        self.cnt_dict = {}
        self.rank_min = []
        self.rank_max = []

    def add(self, num, d=1):
        """要素を1つ追加する

        個数辞書の更新
        昇順順位、降順順位の更新
        Args:
            num (int): 追加要素
        """
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = cnt + d

        heapq.heappush(self.rank_min, num)
        heapq.heappush(self.rank_max, -num)

    def erase(self, num, d=1):
        """要素の削除

        集合から指定要素を指定個数消す。
        順位の更新をする。

        Args:
            num (int): 削除要素
            d (int): 指定個数

        """
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = max(0, cnt - d)
    
    def get_max(self):
        while self.cnt_dict[-self.rank_max[0]] == 0:
            -heapq.heappop(self.rank_max)
        return -self.rank_max[0]

    def get_min(self):
        while self.cnt_dict[self.rank_min[0]] == 0:
            heapq.heappop(self.rank_min)
        return self.rank_min[0]
    
    def __contains__(self, num):
        return self.cnt_dict.get(num, 0) > 0


n, k, q = rm()
al = [0] * n
ms_upper = MultiSet()
ms_upper.add(0, d=k)
ms_lower = MultiSet()
ms_lower.add(0, d=max(n-k, 1))
sum_ = 0
for _ in range(q):
    x, y = rm()
    av = al[x-1]
    al[x-1] = y
    min_ = ms_upper.get_min()
    max_ = ms_lower.get_max()
    if av in ms_upper:
        if y > max_:
            sum_ += y - av
            ms_upper.erase(av)
            ms_upper.add(y)
        else:
            ms_upper.erase(av)
            ms_lower.erase(max_)
            ms_upper.add(max_)
            ms_lower.add(y)
            sum_ += max_ - av
    else:
        if y >= min_:
            sum_ += y - min_
            ms_lower.erase(av)
            ms_upper.erase(min_)
            ms_upper.add(y)
            ms_lower.add(min_)
        else:
            ms_lower.erase(av)
            ms_lower.add(y)
    print(sum_)
