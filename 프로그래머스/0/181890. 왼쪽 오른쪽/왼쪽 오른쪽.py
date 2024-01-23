def solution(str_list):
    answer = []
    idx = 0
    str_set = set(str_list)
    while idx!=len(str_list) and answer==[]:
        if str_list[idx]=="l":
            answer = str_list[:idx]
            break
        elif str_list[idx]=="r":
            if idx == len(str_list)-1: answer = []
            else: answer = str_list[idx+1:]   
            break
        else: pass
        idx += 1
    return answer