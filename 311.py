# 백준
# 수 정렬 4

n = int(input())
answer = []
for i in range (n):
    answer.append(i)
    
answer.sort(reverse=True)

for i in range (n):
    print(answer[i])
