# ABC299-C
# Bより簡単じゃないか？
# 分割して連続'o'の最大長だが、コーナーケースに注意
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
tmp_len = 0
s_ = s.split('-')
ans = max(map(len, s_))
if ans == 0 or (len(s_) == 1 and '-' not in s[0]+s[-1]):
    print(-1)
else:
    print(ans)
