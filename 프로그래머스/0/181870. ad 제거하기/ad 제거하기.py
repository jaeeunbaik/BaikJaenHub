def solution(strArr):
    answer = []
    for i, str in enumerate(strArr):
        if "ad" not in str:
            answer.append(str)
        else: pass
    return answer