# ABC300-D
# 素数リストの生成、リストのスライスが遅いかもしれん
# 適切な範囲の素数リスト作成して、a,b,cの組み合わせを考える
# なるべく計算を減らすために、枝刈り・二分探索も入れた
import sys

ri = lambda: int(sys.stdin.readline())

class PrimeHandler:
    @classmethod
    def get_prime_list(cls, n: int):
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

n = ri()
pl = PrimeHandler.get_prime_list(int(10**5.5))
pl_len = len(pl)
ans = 0
for idx_b, b in enumerate(pl):
    for a in pl[:idx_b]:
        lb = idx_b+1
        ub = pl_len
        tmp = a*a*b
        if lb >= pl_len or tmp*pl[lb]*pl[lb] > n:
            break
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if tmp*pl[mid]*pl[mid] <= n:
                lb = mid
            else:
                ub = mid
        ans += lb - idx_b
print(ans)
