def solution(lottos, win_nums):
    # 순위 딕셔너리 
    dic = {i:j for i, j in zip([6,5,4,3,2,1,0], [1,2,3,4,5,6,6])}
    
    # 일치하는 번호 확인
    temp = [num for num in lottos if num in win_nums]

    # 출력
    return [dic[len(temp)+lottos.count(0)], dic[len(temp)]]