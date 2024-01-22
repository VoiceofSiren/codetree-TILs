n = int(input())
numList = list(map(int, input().split()))

resultList = [0 for _ in range(9)]

for x in numList:
    resultList[x-1] += 1

for x in resultList:
    print(x)