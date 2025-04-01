x = [int(input()) for _ in range(3)]

if sum(x) != 180:
    print('Error')
elif x[0] == x[1] == x[2] == 60:
    print('Equilateral')
elif len(set(x))==2:
    print('Isosceles')
else:
    print('Scalene')