# ABC304-B
# Aより簡単やろ。。
# 文字列長の規則性に気づけば短く書ける
import sys

rr = lambda: sys.stdin.readline().rstrip()

n = rr()
l = len(n)
if l <= 3:
    print(n)
    exit()
l_ = l - 3
print(n[:-l_] + '0'*l_)
