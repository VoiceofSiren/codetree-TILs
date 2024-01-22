inputList = list(map(int, input().split()))

numList = [0, inputList[0], inputList[1]]

for i in range(10):
    numList[0], numList[1], numList[2] =  numList[1], numList[2], (numList[1] + numList[2])%10
    print(numList[0], end=' ')