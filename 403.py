# 이것이 코딩테스트다! -4. 정렬
# 성적이 낮은 순서로 학생 출력하기

n = int(input())
info = {}
scores = []
for i in range (n):
    str, score = input().split()
    info[int(score)] = str
    scores.append(int(score))

scores.sort()
for i in range (len(scores)):
    print(info[scores[i]], end=' ', flush=True)
print()

# solution
n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1]) # key를 기준으로 정렬할 수도 있다. 여기서는 ()의 1번쨰 인덱스에 있는 점수를 가지고 정렬

for student in array:
    print(student[0], end=' ')
