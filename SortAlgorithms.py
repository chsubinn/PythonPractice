# 선택 정렬: 배열 내 최솟값을 차곡차곡 앞으로 보낸다
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range (len(array)):
    min_index = i
    for j in range (i+1, len(array)): # 배열 내 최솟값 찾기
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]
print (array)


# 삽입 정렬: 각 원소가 삽입되어야 할 자리를 찾는다
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range (1, len(array)):
    for j in range (i, 0, -1):
        if array[j]>array[j-1]: # 앞에 있는 원소와 비교했을 때 더 작으면 앞으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break        
print (array)


# 퀵 정렬: 피벗을 기준으로 작은 값, 큰 값 파티션을 만든다 (왼쪽부터 큰 값, 오른쪽부터 작은 값)
# 1.정공법
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def QuickSort (array, start, end):
    if start>=end: 
        return
    pivot = start
    left = start+1
    right = end
    while(left<=right):
        while (left<=end and array[left]<=array[pivot]):
            left+=1 # 왼쪽부터 pivot보다 큰 값 탐색 - 왼쪽이 pivot보다 작으면 한칸 이동
        while (right>start and array[right]>array[pivot]):
            right-=1 # 오른쪽부터 pivot보다 작은 값 탐색 - 오른쪽이 pivot보다 크면 한칸 이동
        if (left>right): # 좌우가 엇갈리면 작은 값과 pivot 교체 
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    QuickSort(array, start, right-1)
    QuickSort(array, right+1, end)

QuickSort(array, 0, len(array)-1)
print(array)

# 2.파이썬의 슬라이싱을 이용한 방법
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def QuickSort (array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]
    return QuickSort(left_side)+[pivot]+QuickSort(right_side)
    
print(QuickSort(array))


# 계수 정렬: 수의 범위가 크지 않을 때, 수가 등장할 때마다 카운트 해준 후 그 카운트 대로 출력한다
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
idx = [0] * (max(array)+1)

for i in range (len(array)):
    idx[array[i]]+=1

for i in range (len(idx)):
    for j in range(idx[i]):
        print(i, end=' ', flush=True)
print()
