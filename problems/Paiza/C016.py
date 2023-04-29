# Paiza-C016
# 辞書を早く書けるか。それを変換するだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

d = {
    'A':'4',
    'E':'3',
    'G':'6',
    'I':'1',
    'O':'0',
    'S':'5',
    'Z':'2',
}
s = rr()
ans = ''
for c in s:
    ans += d.get(c, c)
print(ans)
