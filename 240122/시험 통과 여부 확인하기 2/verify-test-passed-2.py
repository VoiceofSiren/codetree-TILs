n = int(input())
cntValue = 0
for i in range(n):
    scoreList = list(map(int, input().split()))
    if sum(scoreList)/4 >= 60:
        cntValue += 1
        print('pass')
    else:
        print('fail')
print(cntValue)