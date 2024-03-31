# ABC346-B
# 短いので愚直に数える
import sys

rm = lambda: map(int, sys.stdin.readline().split())

s = "wbwbwwbwbwbw" * 20
w, b = rm()
for i in range(len(s) - w - b):
    s_ = s[i : i + w + b]
    if s_.count("w") == w:
        print("Yes")
        exit()
print("No")
