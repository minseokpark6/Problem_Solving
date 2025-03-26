while True:
    # 인풋
    a, b = map(int, input().split())
    # 정지 조건
    if a==0 and b==0:
        break
    # 출력
    if a > b and a%b==0:
        print('multiple')
    elif a<b and b%a==0:
        print('factor')
    else:
        print('neither')