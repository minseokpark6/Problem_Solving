def convert_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 36진법까지 사용 가능
    result = ""

    while n > 0:
        n, remainder = divmod(n, base)
        result = digits[remainder] + result  # 나머지를 앞에 추가

    return result if result else "0"

# 출력
n, b = map(int, input().split())
print(convert_base(n, b))   