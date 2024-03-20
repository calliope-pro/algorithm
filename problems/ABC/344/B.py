# ABC344-B
# A_iが0になるまで入力を受け取って逆順にして出力するだけ
import sys

ri = lambda: int(sys.stdin.readline())

al = []
for _ in range(100):
    av = ri()
    al.append(av)
    if av == 0:
        break
al.reverse()
for av in al:
    print(av)
