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


# solution
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산 -> 계수정렬하듯이 일일이 카운트하지 않아도 된다
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer
