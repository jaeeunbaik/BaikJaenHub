def solution(num_list):
    idx = 0
    while num_list[idx]>=0 and idx!=len(num_list)-1:
        idx += 1
    if idx==len(num_list)-1 and num_list[idx]>=0: idx = -1
    return idx