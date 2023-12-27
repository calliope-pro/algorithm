# ABC329-B
# 重複を消して、ソートして、2番目を出力
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
print(sorted(set(al))[-2])
