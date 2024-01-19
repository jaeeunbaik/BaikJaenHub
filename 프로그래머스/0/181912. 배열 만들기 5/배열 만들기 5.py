def solution(intStrs, k, s, l):
    answer = []
    for Strs in intStrs:
        if int(Strs[s:s+l])>k:
            answer.append(int(Strs[s:s+l]))
        else: pass
        
    return answer