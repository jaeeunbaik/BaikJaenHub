def solution(myString, pat):
    answer = 0
    myString=myString.upper()
    pat=pat.upper()
    if myString.find(pat)!=-1:
        if myString[myString.find(pat):myString.find(pat)+len(pat)]==pat:
            answer=1
        else: answer=1
    else: answer=0
    return answer