inputList = list(map(int, input().split()))

resultList = [inputList[0], inputList[1], inputList[0] * 2 + inputList[1]]

for i in range(10):
    print(resultList[0], end=' ')
    resultList[0], resultList[1], resultList[2] = resultList[1], resultList[2], resultList[1] * 2 + resultList[2]