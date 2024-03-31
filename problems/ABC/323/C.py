# ABC323-C
# にぶたんを駆使すると楽に解ける
import bisect
import itertools
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
al = rl()
scores = []
others = []
for i in range(n):
    s = rr()
    others.append(
        tuple(
            itertools.accumulate(
                [0]
                + sorted((al[si] for si, sv in enumerate(s) if sv == "x"), reverse=True)
            )
        )
    )
    scores.append(i + 1 + sum(al[si] for si, sv in enumerate(s) if sv == "o"))
max_score = max(scores)
for score, other in zip(scores, others):
    if score == max_score:
        print(0)
    else:
        print(bisect.bisect_right(other, max_score - score))
