def solution(myString, pat):
    myString = list(myString)
    for i, str in enumerate(myString):
        if str == "A":
            myString[i]="B"
        elif str=="B":
            myString[i]="A"
    myString = ''.join(myString)
    if pat in myString:
        return 1
    else: return 0