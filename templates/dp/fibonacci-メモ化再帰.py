"""
フィボナッチをメモ化再帰(トップダウンのdp)で実装
fib(0) -> 0
fib(1) -> 1
"""
from typing import List

# メモ結果
dp: List[int]

def fib(n: int) -> int:
    # nがメモ化されているか
    if dp[n] != -1:
        return dp[n]

    # メモ化する
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

if __name__ == '__main__':
    n = 10
    dp = [-1] * (n+1)
    # 初期値fib(0), fib(1)の設定
    dp[0] = 0
    dp[1] = 1
    print(fib(n))

