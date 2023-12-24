# ABC311-A
# A, B, Cに対して、それぞれの文字が最初に出現するインデックスを求め、最大のものを出力するだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
print(max(s.index('A'), s.index('B'), s.index('C'))+1)
