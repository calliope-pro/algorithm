# ABC281-B
# 脳死で正規表現にツッコむ
import sys
import re

rr = lambda: sys.stdin.readline().rstrip()

print('YNeos'[not re.match(r'[A-Z][1-9][0-9]{5}[A-Z]', rr())::2])
