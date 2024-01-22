inputList = list(map(int, input().split()))

diceList = [0 for _ in range(6)]

for x in inputList:
    diceList[x-1] += 1

for i in range(6):
    print(f'{i + 1} - {diceList[i]}')