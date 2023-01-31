# 백준 
# 빙산

n, m = map(int, input().split())
ice = []
for _ in range (n):
    ice.append(list(map(int, input())))
  
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
cracks = 0
def dfs(x, y):
    global cracks
    if 0<=x<n and 0<=y<n:
        for k in range (4):
            nx = x+dx[k]
            ny = y+dy[k]
            dfs(nx, ny)
            cracks += 1
            

def isCracked:
    for x in range (n):
        for y in range (m):
            if ice[x][y]==0: continue
            dfs(x, y)
            if cracks>1:
                return True
            else:
                return False
                    

while True:
    for x in range (n):
        for y in range (m):
            if ice[x][y]==0: continue
            cnt = 0
            for k in range (4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<n and 0<=ny<m and ice[nx][ny]==0:
                    cnt+=1
            if ice[x][y]-cnt>=0: ice[x][y]-=cnt
            else: ice[x][y]=0
            
    if isCracked():
        break
    
print(answer)
        
        
        
