# 재귀를 이용한 이진탐색 알고리즘
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif target<array[mid]:
        return binary_search(array, target, start, mid-1)
    elif array[mid]<target:
        return binary_search(array, target, mid+1, end)
        
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result==None:
    print("Target value is not included")
else:
    print(result+1)
    
# 반복문을 이용한 이진탐색 알고리즘: 반복해서 start, end를 갱신하는 방식
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else:
            start=mid+1
    return None
        
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result==None:
    print("Target value is not included")
else:
    print(result+1)
    

# 파이썬 이진탐색 라이브러리 - 주어진 범위 안에 있는 정수 개수 세기
from bisect import bisect_left, bisect_right

def count_by_range (array, left, right):
    left_cnt = bisect_left(array, left) # 정렬된 순서를 유지하면서 가장 왼쪽에 올 수 있는 인덱스
    right_cnt = bisect_right(array,right) # 정렬된 순서를 유지하면서 가장 오른쪽에 올 수 있는 인덱스
    return right_cnt - left_cnt
    
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))
