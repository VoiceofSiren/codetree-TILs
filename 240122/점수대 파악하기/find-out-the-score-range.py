inputList = list(map(int, input().split()))

resultList = [0 for _ in range(11)]

for i in inputList:
    if i == 0:
        break
    resultList[i//10] += 1

for i in range(10, 0, -1):
    print(f'{i * 10} - {resultList[i]}')