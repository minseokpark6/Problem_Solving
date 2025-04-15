# 입력
arr = sorted(list(map(int, input().split())))
a, b = arr[1], arr[0]
# 유클리드 호제법 
while b!=0:
    a=a%b
    a,b=b,a
# 출력
print((arr[0]*arr[1]) // a)