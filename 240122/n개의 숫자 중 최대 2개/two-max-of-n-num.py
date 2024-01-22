import sys

n = int(input())
inputList = list(map(int, input().split()))

rn1, rn2 = -sys.maxsize, -sys.maxsize
resultList = []

for i in inputList:
    if i > rn1:
        rn1 = i
    else:
        resultList.append(i)

for i in resultList:
    if i > rn2:
        rn2 = i

print(rn1, rn2)