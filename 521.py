# 이것이 코딩테스트다! -5.이진탐색
# 떡복이 떡 만들기

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m: # 결과가 타겟보다 짧으므로 절단기 길이를 줄여줌
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
