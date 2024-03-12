def solution(my_string):
    return sorted([int(i) for i in my_string if i in ['0','1','2','3','4','5','6','7','8','9']])