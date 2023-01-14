# ABC227-A
# a人分だけ番号がズレると考えると計算でいける
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, k, a = rm()
print((a + k - 1) % n or n)
