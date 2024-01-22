def solution(my_string, indices):
    my_list = list(my_string)
    for idx in indices:
        my_list[idx] = ' '
    my_list = ''.join(my_list)
    return my_list.replace(' ','')