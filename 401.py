# 이것이 취업을 위한 코딩 테스트다! -5. 이진 탐색
# 이진 탐색 구현하기 

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split())) #원소 개수와 찾고자 하는 원소
array = list(map(int, input().split())) #전체 원소 배열
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1) #원소의 인덱스 출력
