# ABC268-B
# 接頭辞かどうかは.startsWithメソッド使うだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
print('Yes' if t.startswith(s) else 'No')
