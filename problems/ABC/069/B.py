# ABC069-B
# Pythonのインデックス指定楽ですね
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
print(s[0] + str(len(s) - 2) + s[-1])
