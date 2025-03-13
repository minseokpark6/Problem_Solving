dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
score, credit = 0, 0

for _ in range(20):
    temp = input().split()
    if temp[2] == 'P':
        continue
    score += (float(temp[1])*dic[temp[2]])
    credit += float(temp[1])

print(score/credit)