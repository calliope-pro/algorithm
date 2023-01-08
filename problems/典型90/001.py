# 典型90-001
# 答えの範囲から逆算で導出する
# 問題をうまく読み替える
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, l = rm()
k = ri()
al = [0] + rl() + [l]
al = [b-a for a, b in zip(al, al[1:])]

# [lb, ub)区間を考える
lb = 1
ub = 10**9+10

# m以上の箇所が何か所あるか(最低の長さmがk+1箇所になるまで二分探索)
def f(m: int):
    cnt = 0
    tmp = 0
    for av in al:
        tmp += av
        if tmp >= m:
            cnt += 1
            tmp = 0
    return cnt

while ub - lb > 1:
    mid = (lb + ub) // 2
    if f(mid) >= k+1:
        lb = mid  # midの時はk+1箇所以上 -> mの長さを増やす -> 該当箇所が減る
    else:
        ub = mid  # midの時はk箇所以下 -> mの長さを減らす -> 該当箇所が増える

print(lb)
