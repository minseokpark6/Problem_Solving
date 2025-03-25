'''
총 소요되는 일자 = x 
ax + b(x-1) = v
x = (v-b)/(a-b)
'''
a, b, v = map(int, input().split())
# 변수 지정
x = (v-b)/(a-b)
# 출력
# 정수인 경우
if x == int(x):
    print(int(x))
# 정수가 아닌 경우 >> 하루 추가
else:
    print(int(x)+1)