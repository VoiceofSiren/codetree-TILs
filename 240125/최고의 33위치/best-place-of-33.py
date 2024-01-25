n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]

def count_coins(i, j, square):
    count_value = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            count_value += square[x][y]
    return count_value

max_value = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        max_value = max(max_value, count_coins(i, j, square))
print(max_value)