n = int(input())
num_list = [int(i) for i in input().split()]
num = int(input())

print(len([i for i in num_list if i == num]))