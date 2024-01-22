numList = list(map(int, input().split()))

for x in numList:
    if x == 0:
        break
    print(x%2 == 0 and x//2 or x + 3, end=' ')