import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x, y, z = rm()
a = rl()
b = rl()
scores = []

for i in range(1, n+1):
    scores.append({
        'id': i,
        'math': a[i-1],
        'en': b[i-1],
    })

s = set(range(1, n+1))
scores.sort(key=lambda score: (score['math'], -score['id']), reverse=True)
scores = scores[x:]
scores.sort(key=lambda score: (score['en'], -score['id']), reverse=True)
scores = scores[y:]
scores.sort(key=lambda score: (score['en'] + score['math'], -score['id']), reverse=True)
scores = scores[z:]
s_ = {score['id'] for score in scores}
for i in sorted(s - s_):
    print(i)
