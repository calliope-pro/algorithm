# PAST008-D
# 素因数列挙し、Counterにする
# 約数と素因数の個数の関係より求める
import sys
import math
import collections

rm = lambda: map(int, sys.stdin.readline().split())

class PrimeHandler:
    from typing import List
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
    def prime_factorization(cls, n: int, *, is_decoded: bool=False) -> List[int]:
        '''
        素因数分解し、素因数列挙

        Parameters
        ----------
        n : int
            素因数分解する数
        is_decoded : bool, optional
            展開するか, by default False

        Returns
        -------
        List[int]
            素因数のリスト
            展開している場合は各々の素因数の個数入っている
        '''
        prime_list = []
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

x, y = rm()
c_x = collections.Counter(PrimeHandler.prime_factorization(x, is_decoded=True))
c_y = collections.Counter(PrimeHandler.prime_factorization(y, is_decoded=True))
cnt_x = 1
for v in c_x.values():
    cnt_x *= v+1
cnt_y = 1
for v in c_y.values():
    cnt_y *= v+1
if cnt_x > cnt_y:
    print('X')
    exit()
if cnt_x < cnt_y:
    print('Y')
    exit()
print('Z')
