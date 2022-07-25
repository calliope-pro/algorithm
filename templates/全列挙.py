# 1 5
N, M = map(int, input().split())

def dfs(A):
    if len(A) == N:
        print(A)
        return
    prev_last = A[-1] if len(A) > 0 else 1
    for v in range(prev_last, M+1):
        A.append(v)
        dfs(A)
        A.pop()

dfs([])