# ABC215-D
# エラトステネスの篩を複数回つかえばいい
# 素数列挙はn**0.5まででいい -> 10**2.5の計算量
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
al = rl()
class PrimeHandler:
    from typing import List, Optional, Set
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
    def prime_factorization(cls, n: int, *, is_decoded: bool=False, ps: Optional[List[int]]=None) -> Set[int]:
        '''
        素因数分解し、素因数列挙

        Parameters
        ----------
        n : int
            素因数分解する数
        is_decoded : bool, optional
            展開するか, by default False
        ps : List[int] | None, optional
            事前に準備された素因数のリスト

        Returns
        -------
        Set[int]
            素因数の集合
            展開している場合は各々の素因数の個数入っている
        '''
        prime_list = set()
        if ps is None:
            ps = cls.get_prime_list(math.ceil(n**0.5) + 1)
        for psv in ps:
            if n % psv != 0:
                continue
            while n % psv == 0:
                n //= psv
                if is_decoded:
                    prime_list.add(psv)
            if not is_decoded:
                prime_list.add(psv)
        else:
            if n != 1:
                prime_list.add(n)
        return prime_list

prime_list = PrimeHandler.get_prime_list(math.floor(10**2.5)+5)
set_ = set()
for av in al:
    set_tmp = PrimeHandler.prime_factorization(av, ps=prime_list)
    set_.update(set_tmp)

is_prime_list = [True] * (m+1)
is_prime_list[0] = False
is_prime_list[1] = True
for i in range(2, m+1):
    if is_prime_list[i] and i in set_:
        for j in range(i, m+1, i):
            is_prime_list[j] = False
print(sum(is_prime_list))
for i, is_prime in enumerate(is_prime_list):
    if is_prime:
        print(i)
