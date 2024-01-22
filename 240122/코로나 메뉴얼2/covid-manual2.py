resultList = [0 for _ in range(4)]
for i in range(3):
    inputInfo = input().split()
    a, b = inputInfo[0], int(inputInfo[1])

    if a == 'Y' and b >= 37:
        resultList[0] += 1
    elif a != 'Y' and b >= 37:
        resultList[1] += 1
    elif a == 'Y' and b < 37:
        resultList[2] += 1
    else:
        resultList[3] += 1

for i in resultList:
    print(i, end=' ')
if resultList[0] >= 2:
    print('E')