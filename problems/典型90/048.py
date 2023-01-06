# 典型90-048
# 特殊な制約から性質を見抜く必要がある
# 部分点の加点が満点の過半数であるため、以下のリストを考えられる
# 降順で[部分点a, ..., 満点a]に必ずなる -> sortからのsumするだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
scores = []
for _ in range(n):
    a, b = rm()
    scores.append(b)
    scores.append(a-b)
scores.sort(reverse=True)
print(sum(scores[:k]))
