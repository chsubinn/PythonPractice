# 백준
# Yangjojang of the Year

T = int(input())
for _ in range(T):
    N = int(input())
    max = 0
    Name = ""
    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            Name = name
    print(Name)
