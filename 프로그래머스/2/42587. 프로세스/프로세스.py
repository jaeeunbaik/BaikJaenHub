from collections import deque
def solution(priorities, location):
    answer = 0
    prior = dict()  # prior는 (프로세스, 우선순위) 딕셔너리
    for i, p in enumerate(priorities):
        prior[i] = p
    sorted_prior = sorted(prior.items(), key=lambda x:x[1], reverse=True)
    
    prior = deque(prior.items()) 
    sorted_prior = deque(sorted_prior)
    top = sorted_prior.popleft()[1]
    
    while True:
        temp = prior.popleft()
        if temp[1] == top:
            answer+=1
            if location == temp[0]:
                return answer
            top = sorted_prior.popleft()[1]
        else:
            prior.append(temp)
            
        