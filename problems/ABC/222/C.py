# ABC222-C
# sortとindexの管理だけだからこその難しさ
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
a_matrix = [rr() for _ in range(2*n)]
rounds = [''.join(c) for c in zip(*a_matrix)]
scores = [[0, -i] for i in range(2*n)]
for i in range(m):
    round = rounds[i]
    for j in range(n):
        idx_1 = abs(scores[j*2][1])
        idx_2 = abs(scores[j*2 + 1][1])
        hand1 = round[idx_1]
        hand2 = round[idx_2]
        if hand1 == 'G' and hand2 == 'C':
            scores[j*2][0] += 1
        if hand1 == 'C' and hand2 == 'P':
            scores[j*2][0] += 1
        if hand1 == 'P' and hand2 == 'G':
            scores[j*2][0] += 1
        if hand1 == 'G' and hand2 == 'P':
            scores[j*2 + 1][0] += 1
        if hand1 == 'C' and hand2 == 'G':
            scores[j*2 + 1][0] += 1
        if hand1 == 'P' and hand2 == 'C':
            scores[j*2 + 1][0] += 1
    scores.sort(reverse=True)

for (score, i) in scores:
    print(abs(i) + 1)
