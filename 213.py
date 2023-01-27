# 백준
# 단지 번호 
n = int(input())
graph = []
for _ in range (n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
nums = []
count=0

def dfs (x, y):
    global count
    visited[x][y]=True
    count+=1
    for i in range (4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<n) and (0<=ny<n):
            if visited[nx][ny]==False:
                if graph[nx][ny]!=0:
                    dfs(nx, ny)
    
cnt =0
for i in range (n):
    for j in range (n):
        if visited[i][j]==False and graph[i][j]!=0:
            dfs(i, j)
            nums.append(count)
            cnt += 1
            count=0
            
print(cnt)
nums.sort()
for i in nums:
    print(i)
