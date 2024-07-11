def solution(my_string):
    answer = 0
    c = '0'
    for s in my_string:
        if s.isdigit():
            c += s
        else: 
            answer += int(c)
            c = '0'
    answer += int(c)
    return answer