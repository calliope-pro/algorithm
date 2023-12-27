# AB328-B
# 全探索して、文字列に変換して、setで重複を消して、長さが1ならOK
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
dl = rl()
ans = 0
for m in range(1, n+1):
    for d in range(1, dl[m-1]+1):
        if len(set(str(m)+str(d))) == 1:
            ans += 1
print(ans)
