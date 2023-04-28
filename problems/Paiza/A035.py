# Paiza-A035
# bit全探索に見えた。。。危ない
# dpぽく、1つ前の候補から次の候補をすべて得る
# 16秒なので、一時変数の計算量を考えないでいい
# 合計の候補が高々100なので、100*100で充分速い
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
al = [ri() for _ in range(n)]
ans = set([0])
for i in range(n):
    tmp = set()
    for j in ans:
        tmp.add(al[i] + j)
    ans.update(tmp)
print(len(ans))
for v in sorted(ans):
    print(v)
