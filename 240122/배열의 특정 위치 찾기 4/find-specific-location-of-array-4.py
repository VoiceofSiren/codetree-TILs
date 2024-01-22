intList = list(map(int, input().split()))
resultList = []
for x in intList:
    if x == 0:
        break
    else:
        if x % 2 == 0:
            resultList.append(x)
print(f'{len(resultList)} {sum(resultList)}')