def solution(s):
    answer = []
    for str in set(s):
        if s.count(str) == 1:
            answer.append(str)
    if answer != []:
        return ''.join(sorted(answer))
    return answer