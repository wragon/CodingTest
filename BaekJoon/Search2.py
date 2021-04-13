#%% #1260 Ver.array
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

def dfs(v):
    visit[v] = 1
    print(v, end= ' ')
    for i in range(N+1):
        if not visit[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    visit = [0 for i in range(N + 1)]
    q = [v]
    visit[v] = 1
    while q:
        v = q[0]
        print(v, end = ' ')
        del q[0]
        for i in range(1, N+1):
            if not visit[i] and graph[v][i] == 1:
                q.append(i)
                visit[i] = 1

N, M, V = map(int, input().split())
graph = [[0 for i in range(N + 1)] for j in range(N + 1)]
visit = [0 for i in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(V)
print()
bfs(V)