def solution(sizes):
    # 가로 세로 오름차순 통일
    sorted_sizes = [(max(a,b), min(a,b)) for a, b in sizes]
    # 지갑의 가로*세로 길이 출력
    return max(a for a, _ in sorted_sizes) * max(b for _, b in sorted_sizes)


'''
"
## 이전 통과 코드 

def solution(sizes):
    # 가로 세로 오름차순으로 통일
    sorted_sizes = [sorted(i) for i in sizes]

    # 지갑의 가로 세로 길이 정의
    w = max(size[0] for size in sorted_sizes)
    h = max(size[1] for size in sorted_sizes)

    # 출력
    return w*h

## 문제 풀이 정의

가로 / 세로를 바꿀 수 있다는 것
= 한 쪽에 가로, 세로 중 큰 수를 몰고 / 한 쪽에는 작은 수를 몰아서 
두 리스트에서 가장 큰 수를 뽑아 곱하면 됨
'''