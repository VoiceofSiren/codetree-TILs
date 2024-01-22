intArr = list(map(int, input().split()))
sumVal, countVal = 0, 0
for e in intArr:
    if e < 250:
        sumVal += e
        countVal += 1
    else:
        break
print(f'{sumVal} {sumVal/countVal:.1f}')