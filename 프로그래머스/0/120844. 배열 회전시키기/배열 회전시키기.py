def solution(numbers, direction):
    if direction == "left":
        l1 = numbers[0]
        numbers.remove(l1)
        numbers.append(l1)
        return numbers
    else :
        r1 = numbers[-1]
        numbers.remove(r1)
        numbers.insert(0, r1)
        return numbers