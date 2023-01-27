# 백준
# 적록색약

n = int(input())
graph3 = []
graph2 = []
for i in range (n):
    graph3.append(list(map(str, input())))
    graph2.append(list(map(str, input())))

for i in range (n):
    for j in range (n):
        if graph2[i][j]=='G':
            graph2[i][j]='R'
    print(graph2[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs (x, y, graph):
    color = graph[x][y]
    graph[x][y]=0
    if x<0 or x>=n or y<0 or y>=n:
        return False
    for k in range (4):
        nx = x+dx[k]
        ny = y+dy[k]
        if graph[nx][ny]==color and graph[nx][ny]!=0:
            dfs(nx, ny)
            return True
        else:
            return False
    return False
        
cnt3 =0
for i in range (n):
    for j in range (n):
        if graph[i][j]!=0:
            if dfs (i, j, graph3):
                cnt3+=1
            if dfs (i, j, graph2):
                cnt2+=1
       
print(cnt3)
print(cnt2)
