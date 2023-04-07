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
    print(info[scores[i]], end=' ')
print()
