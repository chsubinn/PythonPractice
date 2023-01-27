# 백준
# DFS/BFS

# my solution
from collections import deque

n, m, k = map(int, input().split())
graph = [[] for _ in range (n+1)]
for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[b].sort()
    graph[a].sort()

print(graph)
visited = [False] * (n+1)

def dfs(v):
    visited[v]=True
    print(v, end=' ', flush=True)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
def bfs(v):
    q = deque()
    visited[v]=True
    q.append(v)
    while q:
        idx = q.popleft()
        print(idx, end=" ", flush=True)
        for j in graph[idx]:
            if not visited[j]:
                visited[j]=True
                q.append(j)
    
    
dfs(k)
visited = [False] * (n+1)
print()
bfs(k)
