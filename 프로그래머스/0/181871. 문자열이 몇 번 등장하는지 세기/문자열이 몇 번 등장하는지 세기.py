def solution(myString, pat):
    cnt=-1
    index = 0
    while index!=-1:
        cnt+=1
        index = myString.find(pat)
        myString=myString[index+1:]
    return cnt