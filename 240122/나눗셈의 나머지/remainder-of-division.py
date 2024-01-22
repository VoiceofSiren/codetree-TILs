a, b = tuple(map(int, input().split()))

resultList = [0 for _ in range(b)]

while a > 1:
    resultList[int(a % b)] += 1
    a /= b

sumVal = 0
for i in resultList:
    sumVal += i**2
print(sumVal)