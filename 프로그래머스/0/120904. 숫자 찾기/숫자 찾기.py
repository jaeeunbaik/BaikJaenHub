def solution(num, k):
    answer = 0
    if str(k) in str(num):
        return str(num).index(str(k)) + 1
    else: return -1
    return answer