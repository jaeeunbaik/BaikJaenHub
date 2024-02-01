def solution(rank, attendance):
    inf = 10e9
    top3 = [0]*3
    for i, att in enumerate(attendance):
        if att:
            pass
        else:
            rank[i]=inf
    for i in range(3):
        top3[i]=rank.index(min(rank))
        rank[rank.index(min(rank))]=inf
    return top3[0]*10000+top3[1]*100+top3[2]