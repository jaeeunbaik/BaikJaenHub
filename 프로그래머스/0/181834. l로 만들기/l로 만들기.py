def solution(myString):
    before_l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    return ''.join(["l" if s in before_l else s for s in myString])