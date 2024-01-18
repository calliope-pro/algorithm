# ABC336-D
# 左にどれだけ階段が続くか、右にどれだけ階段が続くかを記録しておく
# その後、左右の階段の数を比較して、小さい方が作れる段数
# 最後に、その中で最大のものを出力する
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
left = [0] * n
right = [0] * n
for ai, av in enumerate(al):
    left[ai] = min(left[ai - 1] + 1, av)  # 左側の階段の数
for ai, av in enumerate(al[::-1]):
    right[ai] = min(right[ai - 1] + 1, av)  # 右側の階段の数(reverse)
right.reverse()  # もとの順番に戻す
print(max(min(l, r) for l, r in zip(left, right)))
