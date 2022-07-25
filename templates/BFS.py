'''
9 12
0 1
0 4
0 2
1 4
1 3
1 8
3 8
4 8
5 8
5 6
3 7
6 7
'''
n, m = map(int, input().split())
road = [[] for _ in range(m)]
for _ in range(m):
    foo, bar = map(int, input().split())
    road[foo].append(bar)
    road[bar].append(foo)

dist = [-1]*n
dist[0] = 0
stack = [0]
while stack:
    for next_city in road[stack[0]]:
        if dist[next_city] == -1:
            stack.append(next_city)
            dist[next_city] = dist[stack[0]] + 1
    del stack[0]

for i, k in enumerate(dist, 0):
    print(f'{i}までは{k}')

