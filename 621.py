# 백준
# 2579번, 계단 오르기

n = int(input())
stairs = []
for i in range (n):
    stairs.append(int(input()));
    
dp = [0]*(n+1)
dp[0] = stairs[0]
dp[1] = dp[0]+stairs[1]
cnt = 0
for i in range (2, n):
    if (cnt==2):
        dp[i] = dp[i-2]+stairs[i]
        cnt=0
    else:
        dp[i] = dp[i-1]+stairs[i]
        cnt+=1

#10, 20, 45, 55, 75
print(dp)
print(dp[n-1])
