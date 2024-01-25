def solution(my_string, alp):
    my_string = list(my_string)
    for i,e in enumerate(my_string):
        if e==alp:
            my_string[i]=my_string[i].upper()
    return ''.join(my_string)