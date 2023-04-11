# ABC297-C
# 脳死で実装した。答えとして出てくる前の文字を確かめてゴリゴリ条件分岐させた
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
for _ in range(h):
    s = rr()
    ans = ''
    for i in range(w):
        if i < w-1 and s[i] == s[i+1] == 'T':
            if len(ans) > 0 and ans[-1] == 'P':
                ans += 'C'
            else:
                ans += 'P'
        else:
            if len(ans) > 0 and ans[-1] == 'P':
                ans += 'C'
            else:
                ans += s[i]
    print(ans)
