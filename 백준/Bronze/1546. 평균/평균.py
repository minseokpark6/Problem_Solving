n = int(input())
score = [int(i) for i in input().split()]
m = max(score)
new = [i/m*100 for i in score]
print(sum(new)/n)