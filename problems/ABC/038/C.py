# ABC038-C
# 問題名は二分探索なんだけど全然違った
# 貪欲的に単調増加しているかを見て、単調増加が終わったら、あり得る個数を足し合わせる
# 最後に-1を入れることで例外的な処理を行わなくていいハック
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl() + [-1]
ans = 0
tmp = 1
for i in range(n):
    if al[i] < al[i+1]:
        tmp += 1
    else:
        ans += (tmp+1) * tmp // 2
        tmp = 1
print(ans)