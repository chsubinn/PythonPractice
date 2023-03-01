# 이것이 취업을 위한 코딩테스트다! -4. 정렬
# 위에서 아래로

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n):
    print(arr[i], end=' ', flush=True)
print()
