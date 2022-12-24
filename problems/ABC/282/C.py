# ABC282-C
# 真偽値をうまく確保する
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
flag = False
ans = ''
for sv in s:
    if flag == False and sv == ',':
        ans += '.'
        continue
    if sv == '"':
        flag = not flag
    ans += sv
print(ans)
