# ABC337-B
# 順番に出てくる文字種を見ていくだけ。
# パターンが少ないので、全部列挙して一致するかどうかを見た
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()

print(
    "Yes"
    if "".join(k for k, c in itertools.groupby(rr()))
    in {"ABC", "AB", "BC", "AC", "A", "B", "C", ""}
    else "No"
)
