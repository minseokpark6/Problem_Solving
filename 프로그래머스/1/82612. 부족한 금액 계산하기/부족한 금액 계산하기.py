def solution(price, money, count):
    cost = [price*(i+1) for i in range(count)]
    return sum(cost) - money if sum(cost) > money else 0