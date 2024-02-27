def solution(rsp):
    answer = ''
    rsp = list(rsp)
    for i, r in enumerate(rsp):
        if r=="2":
            rsp[i] = "0"
        elif r=="0":
            rsp[i] = "5"
        elif r=="5":
            rsp[i] = "2"
    return ''.join(rsp)