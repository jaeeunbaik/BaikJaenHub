def solution(myString):
    myString = myString.split("x")
    myString.sort()
    while myString[0]=="":
        myString = myString[1:]
    return myString