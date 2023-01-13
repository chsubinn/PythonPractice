# 이것이 코딩 테스트다 - 1.그리디 알고리즘 
# 큰 수의 법칙

# my solution
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
cnt = 0
result = 0
for i in range (m):
    if cnt!=k:
        result+=data[-1]
        cnt+=1
    else:
        result+=data[-2]
        cnt=0     
print(result)

# greedy solution 1 : 반복되는 수열을 파악해서 계산
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
result = 0
arr = data[-1]*k + data[-2] #its length = k+1

result = arr*m//(k+1) + data[-1]*m%(k+1)
print(result)

# greedy solution 2 : 위랑 같은 방식이지만 가장 큰 수가 더해지는 횟수를 따로 계산

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]
result = 0

count = m//(k+1)*k # 가장 큰 수가 더해지는 횟수
count += m%(k+1)

result += count * first
result += (m-count) * second
print(result)


# simple solution
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] #or data[-1]
second = data[n-2] #or data[-2]
result = 0

while True:
  for i in range(k):
    if m==0:
      break
    result+=first
    m-=1  # 더하는 횟수 차감
  if m==0:
    break
  result += second
  m-=1 
print(result)
