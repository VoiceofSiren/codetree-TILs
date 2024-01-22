a, b = tuple(map(int, input().split()))

resultList = [0 for _ in range(b)]

while a > 1:
    resultList[a % b] += 1
    # print(resultList)
    a = a // b

sumVal = 0
for i in resultList:
    sumVal += i**2
print(sumVal)