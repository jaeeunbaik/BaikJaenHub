def solution(myStr):
    myStr = myStr.replace("a", "_").replace("b", "_").replace("c", "_")
    myStr = myStr.split("_")
    myStr = [s for s in myStr if s]
    if myStr == []:
        return ["EMPTY"]
    else: return myStr