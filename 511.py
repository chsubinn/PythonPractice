# 이것이 코딩테스트다! -5. 이진탐색
# 고정점 찾기

# my solution - 반복문 이진 탐색
n = int(input())
arr = list(map(int, input().split()))

def binary_search (arr):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = (start+end+1)//2
        print(mid)
        if arr[mid]==mid:
            return mid
        elif arr[mid]<mid:
            start = mid
        elif arr[mid]>mid:
            end = mid-1
        return -1
    
print(binary_search(arr))

# solution - 재귀함수 이진탐색
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))
index = binary_search(array, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)
