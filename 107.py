# 이것이 코딩테스트다 - 1.그리디 알고리즘
# 곱하기 혹은 더하기

# my solution
S = input()
result = 1
for ch in S:
    if ch == '0': continue
    result *= int(ch)
print(result)

# greedy solution - 0뿐만 아니라 1의 case도 구분
data = input()
result = int(data[0])

for i in range(1, len(data)): #이거 줘야 함..안 그러면 숫자가 작게 나옴
    num = int(data[i])
    if num <= 1 or result <= 1: result += num #result가 1 이하이거나 현재 처리하고 있는 숫자가 1 이하라면 더하기 연산
    else: result *= num
 
print(result)
