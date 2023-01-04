# PAST009-B
# 全ての硬貨をシミュレートする必要はない
# 100での余り、10での余りをシミュレート
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
ans = 0
for _ in range(n):
    a, b = rm()
    remains = b-a
    remains %= 100
    ans += remains//50
    remains %= 10
    ans += remains//5
print(ans)
