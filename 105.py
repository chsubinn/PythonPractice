# 이것이 코딩테스트다 - 1.그리디 알고리즘
# 모험가 길드

# my solution
n = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0

while n != 0:
    cnt = people[-1]
    if n < cnt :
        result += 0
    else:
        result += 1
        n -= cnt
        for i in range (cnt):
            people.pop()

print(result)

# greedy solution
n = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0
count = 0

for i in  data:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count>= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1
        count = 0
print(result)
