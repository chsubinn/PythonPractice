# 이것이 코딩 테스트다 - 1.그리디 알고리즘
# 1이 될 때까지

# my solution
n, k = map(int, input().split())
result = 0

while True:
    if n%k == 0:
        n /=k
        result += 1
    else:
        n -= 1
        result +=1
    if n==1: break

print(result)

# simple solution
n, k = map(int, input().split())
result = 0

while n >= k: # N이 K 이상이라면 K로 계속 나누기
    while n%k !=0:
        n-=1
        result +=1
    n //= k
    result += 1
    
while n>1: #마지막으로 남은 수에 대하여 1씩 빼기
    n-=1
    result += 1
    
print(result)

# greedy solution
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k #target은 n이 k로 나누어떨어지는 수로 변경된 값
    result += (n-target)
    n = target
    if n < k: break # 더 이상 나눌 수 없을 때
    result += 1
    n //= k
    
result += (n-1) # 마지막으로 남은 수에 대하여 1씩 빼기
print(result)
