n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]

def count_coins(row1, col1, row2, col2):
    count_value = 0
    for row in range(row1, row2 + 1):
        for col in range(col1, col2 + 1):
            count_value += square[row][col]
    return count_value


max_value = 0
for i in range(n-2):
    for j in range(n-2):
        if i + 2 >= n or j + 2 >= n:
            continue
        coin_value = count_coins(i, j, i+2, j+2)
        if coin_value > max_value:
            max_value = coin_value
print(max_value)