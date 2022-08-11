# ABC239-D
# 素数列挙とsetを使う
import sys

rm = lambda: map(int, sys.stdin.readline().split())

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

a, b, c, d = rm()
prime_set = set(get_prime_list(201))
for i in range(a, b+1):
    for j in range(c, d+1):
        if (i + j) in prime_set:
            break
    else:
        print('Takahashi')
        exit()
print('Aoki')

