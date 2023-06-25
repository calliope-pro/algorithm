# ABC307-A
# chunk_sizeが決まってる時はrangeとスライスで引っ張ってくるだけ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
ans = []
for i in range(n):
    ans.append(sum(al[i*7:i*7+7]))
print(*ans)
