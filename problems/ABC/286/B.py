# ABC286-B
# .replace使うだけやー
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
print(s.replace('na', 'nya'))
