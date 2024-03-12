def solution(s):
    answer = 0
    s = s.split(' ')
    for idx, ss in enumerate(s):
        if ss == 'Z':
            answer -= int(s[idx-1])
        else: answer += int(ss)
    return answer