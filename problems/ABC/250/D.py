# ABC250-D
# エラトステネスの篩による素数列挙
# 決め打ちでpを選択することでqは二分探索すれば高速実現
import sys
import math

ri = lambda: int(sys.stdin.readline())

def get_prime_list(n: int):
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
    '''
    assert n >= 0, '`n` must be 0 or more.'
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
prime_list = get_prime_list(math.ceil(n**(1/3)))
cnt_primes = len(prime_list)
ans = 0
for i in range(cnt_primes-1):
    prod = prime_list[i]
    left = i
    right = cnt_primes
    while right - left > 1:
        mid = (left + right) // 2
        if prod * (prime_list[mid]**3) <= n:
            left = mid
        else:
            right = mid
    ans += left - i
print(ans)


