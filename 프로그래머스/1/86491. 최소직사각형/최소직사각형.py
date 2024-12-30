def solution(sizes):
    # sizes 오름차순 정렬
    sorted_sizes = [sorted(i) for i in sizes]
    
    # 가로 세로 값 설정
    width = max([i[0] for i in sorted_sizes])
    height = max([i[1] for i in sorted_sizes])
    
    # 출력
    return width * height


"""
가로 / 세로를 바꿀 수 있다는 것
= 한 쪽에 가로, 세로 중 큰 수를 몰고 / 한 쪽에는 작은 수를 몰아서 
두 리스트에서 가장 큰 수를 뽑아 곱하면 됨
"""