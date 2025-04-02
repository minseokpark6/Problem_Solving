while True:
    # 세 변의 길이 인풋
    a, b, c = map(int, input().split())
    # 정지 조건
    if a==0:
        break
    # 최대 값 설정
    m = max(a, b, c)
    # 출력
    if a+b+c-m <= m:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print('Isosceles')
    else:
        print('Scalene')