from collections import OrderedDict

def solution(cacheSize, cities):
    # cacheSize가 0인 경우 
    if cacheSize == 0:
        return len(cities) * 5
    
    # 변수 정의
    cache = OrderedDict()
    time = 0
    
    # 실행시간 구하기 
    for city in map(str.lower, cities):
        if city in cache:
            cache.move_to_end(city)
            time += 1
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.popitem(last=False)   # 맨 앞 요소 제거(last=False)
        
        cache[city] = True
    
    # 출력
    return time

'''
## OrderedDict
- 딕셔너리의 순서를 명시적으로 관리하는 자료구조
- deque vs OrderedDict
    - deque는 이중 연결 리스트
    - 양 끝 삽입 및 삭제 => O(1)
    - 하지만 중간 탐색, 중간 삭제는 => O(n)
    
    - OrderedDict은 해시 테이블(dict) + 이중 연결 리스트 
    - 검색, 삭제, 순서이동 -> O(n)

    - 크기가 커질수록 유의미한 성능 차이가 발생


## 메소드를 사용하지 않은 버전

def solution(cacheSize, cities):
    # cacheSize가 0인 경우 
    if cacheSize == 0:
        return len(cities) * 5
    
    # 변수 정의
    cache = []
    time = 0
    
    # 실행시간 구하기 
    for city in map(str.lower, cities):
        if city in cache:
            cache.remove(city)
            time += 1
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
        
        cache.append(city)
    
    # 출력
    return time


## 개선점
(1) 불필요한 분기(if not memory) 제거
(2) 흩어져 있는 Least Recently Used 캐시 정책 코드 한 번에 처리하는 구조로 변경


## 기존 통과 코드 

def solution(cacheSize, cities):
    # 변수 설정
    answer = 0
    cache = []
    
    # 대소문자 구분 X
    cities = [c.lower() for c in cities]
    
    # 실행시간 구하기
    if cacheSize > 0:
        for city in cities:
            # cache 리스트가 비어있는 경우
            if not cache:
                cache.append(city)
                answer += 5
                continue

            # cache 리스트가 크기만큼 차지 않은 경우
            if len(cache) < cacheSize:
                if city in cache:
                    cache.remove(city)    # LRU 알고리즘 적용
                    cache.append(city)
                    answer += 1
                else:
                    cache.append(city)
                    answer += 5

            # cache 리스트가 꽉 차있는 경우
            else:
                if city in cache:
                    cache.remove(city)    # LRU 알고리즘 적용
                    cache.append(city)
                    answer += 1
                else:
                    cache.append(city)
                    cache.pop(0)
                    answer += 5

    # cacheSize가 0인 경우
    elif cacheSize == 0:
        for _ in range(len(cities)):
            answer += 5
        

    # 출력
    return answer




## 페이지 교체 알고리즘 

FIFO : 페이지가 주기억장치에 적재된 시간을 기준으로 교체될 페이지를 선정하는 기법

단점 : 중요한 페이지가 오래 있었다는 이유만으로 교체되는 불합리. 가장 오래 있었던 페이지는 앞으로 계속 사용될 가능성이 있음.



LFU : 가장 적은 횟수를 참조하는 페이지를 교체

단점 : 참조될 가능성이 많음에도 불구하고 횟수에 의한 방법이므로 최근에 사용된 프로그램을 교체시킬 가능성이 있고, 해당 횟수를 증가시키므로 오버헤드 발생



LRU : 가장 오랫동안 참조되지 않은 페이지를 교체

단점 : 프로세스가 주기억장치에 접근할 때마다 참조된 페이지에 대한 시간을 기록해야함. 큰 오버헤드가 발생


'''