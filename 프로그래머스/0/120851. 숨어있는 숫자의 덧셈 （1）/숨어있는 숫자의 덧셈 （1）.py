def solution(my_string):
    answer=0
    for s in my_string:
        if str.isdigit(s):
            answer+=int(s)
    return answer