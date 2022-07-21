n, m = map(int, input().split())
road = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)

seen = [0]*n
seen[0] = 1
dist = [0]*n
def dfs(lis, city):
    for next_city in lis[city]:
        if seen[next_city] != 1:
            seen[next_city] = 1
            if dist[next_city] > dist[city]:
                dist[next_city] = dist[city] + 1
            dfs(lis, next_city)

dfs(road, 0)
print(dist)

