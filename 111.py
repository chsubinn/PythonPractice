# 이것이 코딩테스트다! -1. 그리디
# 무지의 먹방 라이브

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    lf = len(food_times)
    ft = [0] * lf
    for i in range(lf):
        ft[i] = [food_times[i],i+1]
    ft.sort()
    pre = 0
    for i in range(lf):
        now = ft[i][0]  
        dif = now - pre
        if dif == 0:
            pass
        elif k > dif*lf:
            k -= dif*lf
            pre = now
            
        else:
            k = k%lf
            ft = ft[i:]
            ft.sort(key=lambda x: (x[1], x[0]))
            return ft[k][1]
        lf -= 1
