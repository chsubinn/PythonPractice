# 이것이 코딩테스트다! -6. 다이나믹프로그래밍
# 개미전사

n = int(input())
arr = list(map(int, input().split()))
d = [0] * (n)

d[0] = arr[0]
d[1] = max(d[0], arr[1])

for i in range(2, n):
    d[i]=max(d[i-2]+arr[i], d[i-1])
    print(d) # memo 확인


print(d[n-1])
