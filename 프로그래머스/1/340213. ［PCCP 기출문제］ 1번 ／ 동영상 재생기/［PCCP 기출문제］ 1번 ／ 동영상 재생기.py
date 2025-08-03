def time_to_sec(time):
    m, s = map(int, time.split(":"))
    return m*60 + s

def sec_to_time(t):
    minute, second = t//60, t%60
    return f'{minute:02d}:{second:02d}'

def solution(video_len, pos, op_start, op_end, commands): 
    # 주어진 시간 초 단위로 변경
    l = time_to_sec(video_len)
    now = time_to_sec(pos)
    s, e = time_to_sec(op_start), time_to_sec(op_end)

    # 명령 입력 
    result = now
    for command in commands:
        # 오프닝 구간에 있는지 확인 
        if s <= result < e:
            result = e
        
        # 명령 수행 
        if command == 'prev':
            result -= 10
            if result < 0:
                result = 0
        else:
            result += 10
            if result > l:
                result = l
        
        # 오프닝 구간에 있는지 확인 
        if s <= result < e:
            result = e

    # 출력
    return sec_to_time(result)
