# ABC232-D
# BFSとかDFS使えばいける
# ここではqueueとBFSを使用
import sys
import queue

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
cm = [rr() for _ in range(h)]
cnt = [[0] * w for _ in range(h)]
cnt[0][0] = 1
q = queue.Queue()
q.put((0, 0))
while q.qsize():
    x_now, y_now = q.get()
    if y_now < w-1 and cm[x_now][y_now+1] == '.' and cnt[x_now][y_now+1] == 0:
        cnt[x_now][y_now+1] = cnt[x_now][y_now] + 1
        q.put((x_now, y_now+1))
    if x_now < h-1 and cm[x_now+1][y_now] == '.' and cnt[x_now+1][y_now] == 0:
        cnt[x_now+1][y_now] = cnt[x_now][y_now] + 1
        q.put((x_now+1, y_now))
print(max(list(map(max, cnt))))
