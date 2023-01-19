# 이것이 취업을 위한 코딩테스트다! -2. DFS/BFS
# 특정 거리의 도시 찾기

from collections import deque

n, m, k, x = map(int, input().split())
graph [[] for _ in range (n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#노드의 거리 정보 저장하는 리스트 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 시작 도시의 거리는 0

q = deque([x]) # [x]가 들어있는 큐 만들기
while q:
    now = q.popleft(x)
    for next_node in graph[now]:
        if distance[next_node]==-1:
            distance[next_node]=distance[now]+1
            q.append(next_node)
check = False
for i in range (1, n+1):
    if distance[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)
