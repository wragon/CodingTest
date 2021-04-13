#%% #1260 Ver.list
from collections import deque
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

def dfs(v):
    visit = []
    stack = [v]
    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            stack += reversed(graph[n])
    return visit

def bfs(v):
    visit = []
    queue = deque([v])
    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            queue += graph[n]
    return visit

N, M, V = map(int, input().split())
graph = {i:[] for i in range(1,N+1)}

for i in range(1, M+1): 
    x, y = map(int, input().split()) 
    graph[x].append(y) 
    graph[y].append(x)

for key in graph: 
    graph[key].sort()

print(' '.join(list(map(str,dfs(V))))) 
print(' '.join(list(map(str,bfs(V)))))