n = int(input())
intList = list(map(int, input().split()))
resultList = []
for i in intList:
    if i % 2 == 0:
        resultList.append(i)
for i in resultList[-1::-1]:
    print(i, end=' ')