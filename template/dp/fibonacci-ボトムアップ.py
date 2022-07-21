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

    # 再帰ではなくループで
    for i in range(1, n):
        # dp[i+1]がメモ化されていないとき計算しメモ化
        # メモ化されている箇所はループ内にてスキップ
        if dp[i+1] == -1:
            dp[i+1] = dp[i] + dp[i-1]
    return dp[n]

if __name__ == '__main__':
    n = 20
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    print(fib(n))
    print(dp)