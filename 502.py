# 이것이 코딩테스트다! -5.이진탐색
# 떡복이 떡 만들기

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 적절한 절단기 높이를 이진탐색으로 추정 (절단기의 범위(0~10억)가 아주 넓으므로 이진탐색 사용)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m: # 결과가 타겟보다 짧으므로 절단기 길이를 줄여준다
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
