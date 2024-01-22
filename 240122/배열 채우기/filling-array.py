intList = list(map(int, input().split()))
resultList = []
for x in intList:
    if x != 0:
        resultList.append(x)
    else:
        break
for x in resultList[-1::-1]:
    print(x, end=' ')