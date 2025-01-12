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


"""
# 7번, 17번 반례 케이스 

 0, ["Jeju", "Jeju"]
 
"""


"""
# 페이지 교체 알고리즘 

FIFO : 페이지가 주기억장치에 적재된 시간을 기준으로 교체될 페이지를 선정하는 기법

단점 : 중요한 페이지가 오래 있었다는 이유만으로 교체되는 불합리. 가장 오래 있었던 페이지는 앞으로 계속 사용될 가능성이 있음.



LFU : 가장 적은 횟수를 참조하는 페이지를 교체

단점 : 참조될 가능성이 많음에도 불구하고 횟수에 의한 방법이므로 최근에 사용된 프로그램을 교체시킬 가능성이 있고, 해당 횟수를 증가시키므로 오버헤드 발생



LRU : 가장 오랫동안 참조되지 않은 페이지를 교체

단점 : 프로세스가 주기억장치에 접근할 때마다 참조된 페이지에 대한 시간을 기록해야함. 큰 오버헤드가 발생
"""