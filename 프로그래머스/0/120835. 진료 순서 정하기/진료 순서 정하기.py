def solution(emergency):
    answer = [1]*len(emergency)
    for i, e in enumerate(emergency):
        for em in emergency:
            if e > em:
                pass
            elif e < em:
                answer[i] += 1
            elif e==em:
                pass
    return answer