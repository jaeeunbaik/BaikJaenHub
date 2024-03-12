def solution(my_string):
    my_list = list(my_string)
    for a in ['a', 'e', 'i', 'o', 'u']:
        while a in my_list:
            my_list.remove(a)
    return ''.join(my_list)