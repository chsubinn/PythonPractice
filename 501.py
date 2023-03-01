# 이것이 코딩테스트다! -5.이진탐색
# 부품 찾기

from bisect import bisect_left, bisect_right
n = int(input())
store = list(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))

# 이진탐색으로 풀이
store.sort()
guest.sort()

def find (array, target):
    left = bisect_left(array, target)
    right = bisect_right(array, target)
    return right-left

for i in range (m):
    if find(store, guest[i])>0:
        print("yes", end=' ', flush=True)
    else:
        print("no", end=' ', flush=True)

# 계수정렬로 풀이
cnt = [0]*(max(store)+1)
for i in range (n):
    cnt[store[i]]+=1
for i in range (m):
    if cnt[guest[i]]>0:
        print("yes", end=' ', flush=True)
    else:
        print("no", end=' ', flush=True)

