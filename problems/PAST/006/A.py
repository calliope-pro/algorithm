# PAST006-A
# 前提条件より正規表現使わない仕様で実装
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
if s[3] == '-' and s.count('-') == 1:
    print('Yes')
else:
    print('No')
