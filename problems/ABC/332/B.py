# ABC332-B
# 条件分岐は言われるがままに書く。量はmax, minを使って楽に。
import sys

rm = lambda: map(int, sys.stdin.readline().split())

k, g, m = rm()
g_t, m_t = 0, 0
for _ in range(k):
    if g_t == g:
        g_t = 0
    elif m_t == 0:
        m_t = m
    else:
        g_t, m_t = min(g, g_t + m_t), max(0, g_t + m_t - g)
print(g_t, m_t)
