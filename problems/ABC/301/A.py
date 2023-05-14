# ABC301-A
# TとAの数を比較する
# 同数ならば、最後に出てくる文字で条件分岐すればいい
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
cnt_T = s.count('T')
cnt_A = s.count('A')
if cnt_T > cnt_A:
    print('T')
elif cnt_A > cnt_T:
    print('A')
else:
    print('A' if s[-1] == 'T' else 'T')
