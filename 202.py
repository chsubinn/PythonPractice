# 이것이 취업을 위한 코딩테스트다! -2. DFS/BFS
# 미로 탈출

# my solution: 안돌아감
n, m = map(int, input().split())
graph = []
for i in range (n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs (i, j):
    if i<0 or i>n or j<0 or j>m:
            return False
    for k in range (4):
        if i+dx[k]<0 or i+dx[k]>n or j+dy[k]<0 or j+dy[k]>m:
            return False
        if graph[i+dx[k]][j+dy[k]]==1:
            graph[i+dx[k]][j+dy[k]]=graph[i][j]+1
            bfs(i+dx[k],j+dy[k])
            return True
        else: 
            return False


bfs(1, 1)
print(graph[n-1][m-1])

# solution
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1 
                queue.append((nx, ny))
    return graph[n-1][m-1]
    
print(bfs(0,0))
