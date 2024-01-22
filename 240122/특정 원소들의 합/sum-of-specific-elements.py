tableList = [list(map(int, input().split())) for _ in range(4)]

sum_value = 0

for i in range(4):
    for j in range(4):
        if i >= j:
            sum_value += tableList[i][j]
print(sum_value)