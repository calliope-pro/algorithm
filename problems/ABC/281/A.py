# ABC281-A
# range関数とアンパック
import sys

ri = lambda: int(sys.stdin.readline())

print(*range(ri(), -1, -1), sep='\n')
