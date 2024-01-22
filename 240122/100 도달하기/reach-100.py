n = int(input())
numList = [1, n, n+1]
while True:
    print(numList[0], end=' ')
    if numList[0] > 100:
        break
    numList[0], numList[1], numList[2] = numList[1], numList[2], numList[1] + numList[2]