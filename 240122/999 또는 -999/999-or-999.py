import sys

inputList = list(map(int, input().split()))
max_value, min_value = -sys.maxsize, sys.maxsize

resultList = []
for i in inputList:
    if i == 999 or i == -999:
        break
    resultList.append(i)

for i in resultList:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print(max_value, min_value)