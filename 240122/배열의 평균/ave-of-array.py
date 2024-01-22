tableList = []
for i in range(2):
    rowList = list(map(int, input().split()))
    tableList.append(rowList)


for i in range(2):
    print(f'{sum(tableList[i])/4:.1f}', end=' ')
print()

for i in range(4):
    sum_value = 0
    for j in range(2):
        sum_value += tableList[j][i]
    print(f'{sum_value/2:.1f}', end=' ')
print()

sum_result = 0
for i in range(2):
    for j in range(4):
        sum_result += tableList[i][j]
print(f'{sum_result/8:.1f}')