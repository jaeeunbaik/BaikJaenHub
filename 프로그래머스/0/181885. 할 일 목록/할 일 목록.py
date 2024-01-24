def solution(todo_list, finished):
    answer = []
    for idx in range(len(finished)):
        if finished[idx]:
            pass
        else: answer.append(todo_list[idx])
    return answer