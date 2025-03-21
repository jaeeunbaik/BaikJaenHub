def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    # 1번 부터 차례대로 도난 당했는지 검사, 
    # 도난 안당했으면 그냥 넘어감 + 1
    # 도난 당했으면 주변에 여벌있는지 검사, 여벌 없으면 continue
    # 도난 당했는데 주변에 여벌있으면 내 자신인지 검사, 
    # 내 자신이면 reserve에서 빼고 + 1
    # 내 자신이 아니면 reserve에서 빼고 + 1
    temp_r = reserve.copy()
    temp_l = lost.copy()
    for r in reserve:
        if r in lost:  # 만약에 여분이 있는데 내가 잃어버렸다.
            temp_r.remove(r)  # 그러면 여분있는 사람 리스트에서 제외함. 
            temp_l.remove(r)  # 도난 당한 사람 리스트에서도 제외함.
    reserve = temp_r
    lost = temp_l
    for i in range(1, n+1):
        if i in lost:  # 만약 i 번 학생이 잃어버렸다, 
            for d in [-1, 1]:  # 주변 학생 물어봐
                if i + d in reserve:  # 주변 학생 있으면, 
                    reserve.remove(i + d)
                    answer += 1  # 빌려줘
                    print(i)
                    break
        else:  # 잃어버리지 않
            answer += 1
            
    return answer