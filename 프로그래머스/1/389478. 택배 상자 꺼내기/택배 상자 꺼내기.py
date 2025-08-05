def solution(n, w, num):
    # 상자를 가득 쌓은 층, 남은 상자 개수 정의
    floor, left = n//w, n%w

    # 꺼내야할 상자 위치 확인 
    row = (num - 1) // w  # 몇 번째 층(행)에 있는지
    col = (num - 1) % w   # 그 층에서 몇 번째 위치인지

    # 역방향일 경우 실제 위치를 반대로 계산
    if row % 2 == 1:
        col = w - 1 - col

    # 상자 쌓기
    temp = [i for i in range(1, n+1)]
    box = [temp[w*idx:w*(idx+1)] if idx%2==0 else sorted(temp[w*idx:w*(idx+1)], reverse = True) for idx in range(n//w)]

    # 남은 상자가 있을 경우 마저 쌓기
    if left != 0:
        # 정방향
        if floor%2 == 0:
            arr = temp[w*(n//w):] + ["X" for _ in range(w-left)]
        # 역방향
        else:
            arr = ["X" for _ in range(w-left)] + sorted(temp[w*(n//w):], reverse=True)

        box.append(arr)

    # 꺼내야 하는 상자 개수 카운트 
    result = [box[i][col] for i in range(row, len(box)) if box[i][col] !='X']

    # 출력
    return len(result)
