def solution(array):
    cnt = 0
    for num in array:
        for n in str(num):
            if '7' in str(n):
                cnt += 1
    return cnt