n, m = tuple(map(int, input().split()))
square = [
    list(map(int, input().split()))
    for _ in range(n)
]

#    EE  SE SS SW WW NW  NN  NE
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max_value(x, y, square):
    max_value = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value

def get_position_to_change(x, y, square):
    max_value = get_max_value(x, y, square)
    position_to_change = (0, 0)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        if max_value == square[nx][ny]:
            position_to_change = (nx, ny)
            break
    return position_to_change

def change_all(square):
    for num in range(1, n * n + 1):
        if_changed = False
        for i in range(n):
            for j in range(n):
                if if_changed == True:
                    continue
                if square[i][j] == num:
                    # x, y: current_position
                    x, y = i, j
                    # p, q: position_to_change
                    p, q = get_position_to_change(x, y, square)
                    square[p][q], square[x][y] = square[x][y], square[p][q]
                    if_changed = True


for _ in range(m):
    change_all(square)

for row in square:
    for element in row:
        print(element, end=' ')
    print()