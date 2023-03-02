# 이것이 코딩테스트다!-4. 정렬
# 국영수

n = int(input())
info = []
for i in range (n):
    info.append(input().split())
    
info.sort(reverse = True, key=lambda student: (int(student[1]), -int(student[2]), int(student[3]), -ord(student[0][0])))
# '-' 기호를 사용해서 이전 순서의 역순으로 정렬 가능
# '-'를 사용하려면 int, ord 등으로 문자열을 숫자로 변환해줘야 한다.
for i in info:
    print(i[0])
