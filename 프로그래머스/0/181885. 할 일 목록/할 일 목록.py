def solution(todo_list, finished):
    answer = []
    for idx, todo in enumerate(todo_list):
        if finished[idx] == False:
            answer.append(todo)
    return answer