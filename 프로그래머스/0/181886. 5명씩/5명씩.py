def solution(names):
    answer = []
    # 나뉘는 그룹 수 지정
    if len(names) % 5 == 0:
        n = len(names) // 5
    else:
        n = ((len(names)) // 5) + 1
    # 각 그룹의 첫 번째로 오는 사람 리스트에 담기
    for i in range(n):
        answer.append(names[5 * i])
    return answer