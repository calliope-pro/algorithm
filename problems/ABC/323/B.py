# ABC323-B
# カウントしてソートするだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
sl = []
for i in range(n):
    score = rr()
    sl.append((i+1, score.count('o')))
sl.sort(key=lambda x: (-x[1], x[0]))
for s in sl:
    print(s[0])
