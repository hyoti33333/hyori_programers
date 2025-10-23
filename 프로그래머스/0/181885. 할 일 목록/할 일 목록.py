def solution(todo_list, finished):
    return [todo_list[i] for i, f in enumerate(finished) if not f]