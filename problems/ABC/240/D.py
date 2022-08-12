# ABC240-D
# stackやdequeを使う。総計出すために変数使うことで計算量を減らす
import sys
import queue

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
stack = queue.LifoQueue()
ans = 0
for av in a:
    if not stack.empty():
        last_v, last_cnt = stack.get()
    else:
        last_v, last_cnt = av, 0
    if av == last_v:
        if 1 + last_cnt == av:
            ans -= last_cnt
        else:
            stack.put((av, last_cnt + 1))
            ans += 1
    else:
        stack.put((last_v, last_cnt))
        stack.put((av, 1))
        ans += 1
    print(ans)
