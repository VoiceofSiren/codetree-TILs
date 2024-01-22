n = int(input())
intList = list(map(int, input().split()))
for x in intList:
    if x % 2 == 0:
        print(x, end=' ')