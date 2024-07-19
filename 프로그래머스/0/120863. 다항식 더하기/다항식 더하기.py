def solution(polynomial):
    x = []
    num = []

    poly = polynomial.split(' ')


    for i in poly:
        if i == 'x':
            i = i.replace('x', '1')
            x.append(int(i))
        elif 'x' in i:
            i = i.replace('x', '')
            x.append(int(i))
        elif i == '+':
            pass
        else:
            num.append(int(i))

    plus = ' ' + '+' + ' ' 
    
    if sum(x) == 0:
        answer = str(sum(num))
    elif sum(x) == 1 and sum(num) == 0:
        answer = 'x'
    elif sum(x) == 1 and sum(num) > 0:
        answer = 'x' + plus + str(sum(num))
    elif sum(x) > 1 and sum(num) == 0:
        answer = str(sum(x)) + 'x'
    else :
        answer = str(sum(x)) + 'x' + plus + str(sum(num))

        
    return answer