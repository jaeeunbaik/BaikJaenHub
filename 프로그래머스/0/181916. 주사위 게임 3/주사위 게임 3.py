def solution(a, b, c, d):
    answer = 0
    dice = [a,b,c,d]
    dice_set = list(set(dice))
    
    if dice.count(a)==4:
        answer = 1111*a
    elif (len(dice_set)==2) and (dice.count(dice_set[0])==2 & dice.count(dice_set[1])==2):
        answer = (dice_set[0]+dice_set[1])*abs(dice_set[0]-dice_set[1])
        
    elif (len(dice_set)==2) and (dice.count(dice_set[0])==3):
        answer = (10*dice_set[0]+dice_set[1])**2
        
    elif (len(dice_set)==2) and (dice.count(dice_set[0])==1):
        answer = (10*dice_set[1]+dice_set[0])**2
    elif len(dice_set)==3:
        if dice.count(dice_set[0])==2:
            answer = dice_set[1]*dice_set[2]
        elif dice.count(dice_set[1])==2:
            answer = dice_set[2]*dice_set[0]
        elif dice.count(dice_set[2])==2:
            answer = dice_set[1]*dice_set[0]
        else: pass
    elif len(dice_set)==4:
        answer = min(dice_set)
            
    return answer