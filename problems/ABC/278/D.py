# ABC278-D
# 全ての要素を上書きするとN^2掛かる
# 各要素が使われる時だけ、シミュレートできるようにすればいい
# それぞれの要素に対して最終更新位置をメモ
# 上書きの情報を常にグローバルで保持
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
last_reset_idxs = [-1]*n  # 最後に更新されたときの番号
q = ri()
last_reset = (-1, -1)  # (i番目, value)
for i in range(q):
    query = rl()
    if query[0] == 1:
        last_reset = (i, query[1])
    elif query[0] == 2:
        if last_reset_idxs[query[1] - 1] < last_reset[0]:
            al[query[1] - 1] = last_reset[1] + query[2]
        else:
            al[query[1] - 1] += query[2]
        last_reset_idxs[query[1] - 1] = i
    else:
        if last_reset_idxs[query[1] - 1] < last_reset[0]:
            print(last_reset[1])
        else:
            print(al[query[1] - 1])
            last_reset_idxs[query[1] - 1] = i
