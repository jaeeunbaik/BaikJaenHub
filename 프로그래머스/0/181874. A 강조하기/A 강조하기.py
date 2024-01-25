def solution(myString):
    myString = list(myString)
    for i,a in enumerate(myString):
        if a=="a" or a=="A":
            myString[i]="A"
        else: myString[i] = myString[i].lower()
    return ''.join(myString)