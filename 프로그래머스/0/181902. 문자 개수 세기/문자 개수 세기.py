import string
def solution(my_string):
    alphabet = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    answer = {}
    for a in alphabet:
        if a in my_string:
            answer[a] = my_string.count(a)
        else: answer[a] = 0
    return list(answer.values())