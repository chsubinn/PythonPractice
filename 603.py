# 이것이 코딩테스트다! -6. 다이나믹 프로그래밍
# 바닥 공사

n = int(input())

d = [0] * (n+1)

d[1] = 1
d[2] = 3

# 왼쪽부터 i-1 까지의 길이가 이미 덮개로 채워져 있으면, i 번째를 채우는 방법은 2 x 1 의 덮개를 채우는 하나의 경우밖에 없습니다.
# 왼쪽부터 i-2 까지의 길이가 이미 덮개로 채워져 있으면, i-1 번째와 i 번째를 채우는 방법은 1 x 2 덮개 2개를 넣는 경우, 혹은 2 x 2 의 덮개 하나를 넣는 경우로, 2가지 경우가 존재합니다.

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796
    print(d)

print(d[n])
