"""
二次配列を用いたdp
p(5) -> [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 4], [5], [1, 2, 2], [2, 3]の7つ
pに関する漸化式を立てるのは難しい

漸化式
q(k, n)を考える
q(k, n)は「k以下の数のみを用いた場合のnの分割数」
q(0, 0) = 1
q(0, n) = 0 {n >= 1}
q(k, n) = q(n, n) {k > n >= 0}
q(k, n) = q(k-1, n) + q(k, n-k) {n >= k >= 1}

p(n) = q(n, n)が満たせる
"""
from typing import List

# 愚直な漸化式
def q_naive(k: int, n: int) -> int:
    if k == 0 and n == 0:
        return 1
    if k == 0:
        return 0
    if k > n:
        return q_naive(n, n)
    return q_naive(k-1, n) + q_naive(k, n-k)


# 二次元配列dp_topdownを用いる
dp_topdown: List[List[int]]
# トップダウン型
def q_dp_topdown(k: int, n: int) -> int:
    # 関心の分離を念頭に置く。(returnとメモ化は分離)

    # メモ化されているか
    if dp_topdown[k][n] != -1:
        return dp_topdown[k][n]
    
    # 漸化式にてメモ化を行う(初期値はmain内で行ってもよい)
    if k == 0 and n == 0:
        dp_topdown[k][n] = 1
    elif k == 0:
        dp_topdown[k][n] = 0
    elif k > n:
        dp_topdown[k][n] = q_dp_topdown(n, n)
    else:
        dp_topdown[k][n] = q_dp_topdown(k-1, n) + q_dp_topdown(k, n-k)
    # メモ化後に計算・保存された値を返す
    return dp_topdown[k][n]


# 二次元配列dp_bottomupを用いる
dp_bottomup: List[List[int]]
# ボトムアップ型(0, 0) -> (n, n)に対して1行ごとに走査すればよい
def q_dp_bottomup(k: int, n: int) -> int:
    # 初期化されてない1行目以降
    for j in range(1, n+1):
        for i in range(0, j):
            # i < kであるため
            dp_bottomup[j][i] = dp_bottomup[i][i]
        for i in range(j, n+1):
            # 配列における上のマスと左のマスを足す
            dp_bottomup[j][i] = dp_bottomup[j-1][i] + dp_bottomup[j][i-j]
    # 計算・保存された値を返す
    return dp_bottomup[k][n]

if __name__ == '__main__':
    n = 50
    dp_topdown = [[-1]*(n+1) for _ in range(n+1)]
    # 初期値設定
    dp_bottomup = [[0]*(n+1)] + [[-1]*(n+1) for _ in range(n)]
    dp_bottomup[0][0] = 1
    print(q_naive(n, n))
    print(q_dp_topdown(n, n))
    print(q_dp_bottomup(n, n))

