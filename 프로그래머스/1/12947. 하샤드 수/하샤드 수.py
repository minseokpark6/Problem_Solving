def solution(x):
    # 변수 정의
    s = sum(int(i) for i in str(x))
    # 출력 
    return True if x%s==0 else False

'''
(1) 제너레이터 표현식 vs 리스트 컴프리헨션
- 굳이 리스트에 한 번 저장을 해서 sum에 보낼 필요가 없음 
- 리스트를 만들지 않고, 하나씩 꺼내서 바로 sum에 전달
- 메모리를 거의 쓰지 않고, 필요할 때마다 "즉석에서 생성"
- 즉, 이터레이터를 만들어서 순차적으로 값을 생산
'''


'''
def solution(x):
    # 각 자리 수의 합 구하기
    x_list = [int(i) for i in str(x)]
    s = sum(x_list)
    # 하샤드 수 검사
    if x % s == 0:
        return True
    else:
        return False
'''