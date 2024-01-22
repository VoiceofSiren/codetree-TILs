n = int(input())
numList = [n * i for i in range(1, 11)]

cntValue = 0
for x in numList:
    if cntValue == 2:
        break
    print(x, end=' ')
    if x % 5 == 0:
        cntValue += 1