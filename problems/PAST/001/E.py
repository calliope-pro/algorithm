# PAST001-E
# 制約が小さいので、3重ループでごり押し
# 3ではフォロー状態が変化するので、フォローする人を集合で管理したりすると良い
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
dp = [[0]*n for _ in range(n)]
for aa in range(q):
    s_ = rl()
    if s_[0] == 1:
        a = s_[1] - 1
        b = s_[2] - 1
        dp[a][b] = 1

    if s_[0] == 2:
        a = s_[1] - 1
        for i, dp_ in enumerate(dp):
            if dp_[a] == 1 and i != a:
                dp[a][i] = 1

    if s_[0] == 3:
        a = s_[1] - 1
        set_ = set()
        for i, dp_1 in enumerate(dp[a]):
            if dp_1 == 1:
                for j, dp_2 in enumerate(dp[i]):
                    if dp_2 == 1 and j != a:
                        set_.add(j)
        for j in set_:
            dp[a][j] = 1
for dp_ in dp:
    print(''.join('NY'[c] for c in dp_))

