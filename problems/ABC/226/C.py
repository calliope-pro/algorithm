# ABC226-C
# 習得すべき技の集合を用意し、最後にそれらに必要な時間を足し合わせると良い
# わざわざdfs等で時間をメモする必要はない
import sys
import queue

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
skills = []
for i in range(n-1):
    t, k, *al = rl()
    skills.append((t, al))
t, k, *al = rl()
q = queue.Queue()
for av in al:
    q.put(av)

skill_set = set(al)
while q.qsize():
    skill_idx = q.get() - 1
    for skill in skills[skill_idx][1]:
        if skill not in skill_set:
            skill_set.add(skill)
            q.put(skill)
ans = t
for k in skill_set:
    ans += skills[k-1][0]
print(ans)
