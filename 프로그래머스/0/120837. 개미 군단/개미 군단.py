def solution(hp):
    a = 0
    answer = align(hp, a)
    return answer

def align(tmp_hp, answer):
    if tmp_hp >= 5:
        tmp_hp -= 5
        answer += 1
        return align(tmp_hp, answer)
    elif tmp_hp >= 3:
        tmp_hp -=3
        answer += 1
        return align(tmp_hp, answer)
    elif tmp_hp >= 1:
        tmp_hp -=1
        answer += 1
        return align(tmp_hp, answer)
    elif tmp_hp == 0:
        return answer