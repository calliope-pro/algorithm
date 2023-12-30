# ABC324-B
# for文をなるべく減らすループ
import sys
import math

ri = lambda: int(sys.stdin.readline())

n = ri()
for i in range(60):
    if n % 3**i == 0:
        e = math.floor(math.log2(n // 3**i))
        for j in range(e-1, e+2):
            if n // 3**i % 2**j == 0:
                print('Yes')
                exit()
print('No')
