inputList = list(map(int, input().split()))

resultList = [0 for _ in range(10)]

for i in inputList:
    if i == 0:
        break
    resultList[i//10] += 1
for i in range(1, 10):
    print(f'{i} - {resultList[i]}')