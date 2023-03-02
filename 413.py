# 이것이 코딩테스트다! -4. 정렬
# 실패율

# my solution
N = int(input())
stages = list(map(int, input().split()))
users = len(stages)

cnt = [0]*(N+1)
lose = []
for s in stages:
    if s==N+1: continue
    cnt[s]+=1

for i in range (1, len(cnt)):
    users -= cnt[i-1]
    lose.append((i, float(cnt[i]/users)))
    
lose.sort(reverse=True, key=lambda stage : stage[1])
print(lose)
answer = []
for i in range (N):
    answer.append(lose[i][0])

print(answer)
