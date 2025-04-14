import sys 
input = sys.stdin.readline
# 입력 
n, m = map(int, input().split())
# 딕셔너리 생성
name_to_num = {}
num_to_name = {}
# 포켓몬 사전 입력
for i in range(1, n+1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[str(i)] = name 
# 출력
for _ in range(m):
    temp = input().strip()
    print(name_to_num[temp] if temp in name_to_num else num_to_name[temp])