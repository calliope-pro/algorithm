# ABC253-C
# multisetを拝借した。
# 理解できるシンプルなもので通した
import sys
import heapq

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

class MultiSet:
    """多重集合

    重複する整数の集合を保持する

    """
    def __init__(self):
        self.cnt_dict = {}
        self.rank_min = []
        self.rank_max = []

    def add(self, num):
        """要素を1つ追加する

        個数辞書の更新
        昇順順位、降順順位の更新
        Args:
            num (int): 追加要素
        """
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = cnt + 1

        heapq.heappush(self.rank_min, num)
        heapq.heappush(self.rank_max, -num)

    def erase(self, num, d):
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

q = ri()
m = MultiSet()
for _ in range(q):
    query = rl()
    if query[0] == 1:
        m.add(query[1])
    if query[0] == 2:
        m.erase(query[1], query[2])
    if query[0] == 3:
        print(m.get_max() - m.get_min())
