def solution(strArr):
    answer = [0]*100000
    for str in strArr:
        answer[len(str)]+=1
    return max(answer)