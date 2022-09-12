# ABC267-B
# ピンの状態をpinsで管理
# 左端と右端の0を抜いて中に0があるのかを判断
import sys

rr = lambda: sys.stdin.readline().rstrip()

pins = [{7}, {4}, {2, 8}, {5}, {3, 9}, {6}, {10}]

s = rr()
sl = [int(sv)==0 and i for i, sv in enumerate(s, 1)]
if sl[0] != 1:
    print('No')
    exit()
for sv in sl[1:]:
    for pin in pins:
        pin.discard(sv)
pin_cnts = ''.join(map(lambda pin: str(len(pin)), pins))
pin_cnts = pin_cnts.strip('0')
if '0' in pin_cnts:
    print('Yes')
else:
    print('No')
