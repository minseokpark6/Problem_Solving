n = int(input())
i = 2
# 소인수분해
while n > 1:
    if n%i==0:
        n = n//i
        print(i)
    else:
        i+=1