# 이것이 코딩테스트다! -4. 정렬
# 안테나

n = int(input())
house = list(map(int, input().split()))

house.sort()
answer = house[(n-1)//2]
print(answer)
