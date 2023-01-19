# 이것이 취업을 위한 코딩테스트다! -2. DFS/BFS
# 음료수 얼려 먹기

# My Solution

n, m = map(int, input(). split())
graph = []
for i in range (n):
    graph.append(list(map(int, input())))
    
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs (i, j):
    if  0 > i and i >= m  and 0 > j  and j >= n :
            return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        for k in range (4):
            dfs(i+dx[k], j+dy[k])
        return True
    return False

cnt = 0
for i in range (n):
    for j in range (m):
        if dfs(i, j) == True:
            cnt+=1
print(cnt)
