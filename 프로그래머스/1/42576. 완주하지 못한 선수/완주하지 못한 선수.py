def solution(participant, completion):
    # 해시 : k, v dict 생성
    # participant 딕셔너리랑 completion 딕셔너리 생성 (이름, 숫자)
    # 이름 알파벳 순으로 배열
    # key 하나씩 비교하면서 다른 그 순간 ! return~
    par = {}
    for i, p in enumerate(sorted(participant)):
        par[i] = p
    com = {}
    for i, c in enumerate(sorted(completion)):
        com[i] = c
    com[len(com)] = 0
    for k, v in par.items():
        if par[k] != com[k]:
            return v
    
    