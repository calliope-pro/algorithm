# 典型90-002
# 偶数の判定をまずすること
# 制約が小さいため、文字列の全探索を行い、適切かどうかを逐一判定する
import sys
import itertools

ri = lambda: int(sys.stdin.readline())

n = ri()
if n&1:
    exit()
for comb in itertools.product('()', repeat=n):
    s = ''.join(comb)
    tmp = 0
    for c in s:
        if c == '(':
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            break
    else:
        if tmp == 0:
            print(s)
