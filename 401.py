# 이것이 취업을 위한 코딩테스트다! -4.정렬
# 두 배열의 원소 교체

# my solution
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
for i in range (n-1, n-k-1, -1):
    a[n-i-1] = b[i]
    
print(sum(a))

# solution
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
