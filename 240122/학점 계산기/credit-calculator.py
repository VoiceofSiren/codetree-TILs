n = int(input())
scoreList = list(map(float, input().split()))
averageScore = 0
for s in scoreList:
    averageScore += s
averageScore /= n
print(f'{averageScore:.1f}')
if averageScore >= 4.0:
    print('Perfect')
elif averageScore >= 3.0:
    print('Good')
else:
    print('Poor')