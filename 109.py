# 이것이 코딩테스트다 -1.그리디 알고리즘
# 볼링공 고르기

# my solution
n, m = map(int, input().split())
balls = list(map(int, input().split()))
#전체 경우의 수 세기
result = 0
cnt = n - 1
while cnt > 0:
    result += cnt
    cnt -= 1
#무게가 같은 경우 전체 경우의 수에서 제외
for i in range (n-1):
    for j in range (i+1, n):
        if balls[i]==balls[j] and i!=j:
            result-=1
print(result)


# greedy solution
n, m = map(int, input().split())
balls = list(map(int, input().split()))

array = [0] * 11
for x in data:
    array[x] += 1
result = 0
for i in range (1, m+1):
    n-=array[i] # A가 선택할 수 있는 개수 제외
    result += array[i] * n #B가 선택하는 경우의 수와 곱하기
print(result)
    
