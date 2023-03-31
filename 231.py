# 이것이 코딩테스드다! -DFS/BFS
# 문자열 압축

# my solution
def solution(s):
    shortest = len(s)
    for i in range(1, (len(s)//2)+1):
        tmp = []
        count = 1
        tmp_str = ""
        idx = 0
        while idx < len(s)+i:
            tmp.append(s[idx: idx+i])
            idx += i
            
        for k in range(0, len(tmp)-1):
            if tmp[k] != tmp[k+1]:
                if count ==1:
                    tmp_str += tmp[k]
                else:
                    tmp_str += str(count) + tmp[k]
                    count = 1
            else:
                count+=1
        shortest = min(len(tmp_str), shortest)
    return shortest
  
# solution
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
