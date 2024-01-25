def solution(strArr):
    for i, e in enumerate(strArr):
        if i%2==0:
            strArr[i]=e.lower()
        elif i%2==1:
            strArr[i]=e.upper()
    return strArr