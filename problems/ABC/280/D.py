# ABC280-D
# 難しくみえるけど、結構脳死でいい
# これぐらいなら素因数分解してそれぞれの素因数に関して単にループして個数取得すればいい。
import sys
import math
import collections
from typing import List, Optional

ri = lambda: int(sys.stdin.readline())

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

k = ri()
pc = collections.Counter(PrimeHandler.prime_factorization(k, is_decoded=True))
ans = 0
for p, c in pc.items():
    i = 0
    while c > 0:
        i += 1
        a = i*p
        while a%p == 0:
            a //= p
            c -= 1
    ans = max(i*p, ans)
print(ans)
