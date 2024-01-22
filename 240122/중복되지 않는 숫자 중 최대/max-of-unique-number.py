import sys

n = int(input())
inputList = list(map(int, input().split()))

resultList = [0 for _ in range(1000)]

for i in inputList:
    resultList[i] += 1
#print(resultList)
filteredList = [0 for _ in range(1000)]

for i in range(len(resultList)):
    if resultList[i] >= 2:
        continue
    else:
        filteredList[i] = resultList[i]
#print(filteredList)
max_value, cnt_value = -sys.maxsize, 0

for i in range(len(filteredList)):
    if filteredList[i] == 1:
        max_value = i
    if filteredList[i] != 0:
        cnt_value += 1

if cnt_value == 0:
    print(-1)
else:
    print(max_value)