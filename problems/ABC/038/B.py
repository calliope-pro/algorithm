# ABC038-B
# 単にaの中のものがbに含まれるかを調べればいい
# 制約小さいので普通に実装
import sys
 
rl = lambda: list(map(int, sys.stdin.readline().split()))
 
a = rl()
b = rl()
for i in a:
    if i in b:
        print('YES')
        exit()
print('NO')
