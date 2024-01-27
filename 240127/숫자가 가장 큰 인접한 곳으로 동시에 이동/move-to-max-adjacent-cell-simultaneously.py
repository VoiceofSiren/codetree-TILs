n, m, t = tuple(map(int, input().split()))

square = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp_count = [
    [0 for j in range(n)]
    for i in range(n)
]

count = [
    [0 for j in range(n)]
    for i in range(n)
]

#      N  S  W  E
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_next_position(x, y, square):
    max_value = 0
    next_position = (0, 0)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and square[nx][ny] > max_value:
            max_value = square[nx][ny]
            next_position = (nx, ny)
    return next_position

def move(x, y):
    nx, ny = get_next_position(x, y, square)
    temp_count[nx][ny] += 1

def move_all(x, y, square):
    for i in range(n):
        for j in range(n):
            temp_count[i][j] = 0
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    for i in range(n):
        for j in range(n):
            count[i][j] = temp_count[i][j]

def remove_duplicates():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

def simulate(x, y, square):
    move_all(x, y, square)
    remove_duplicates()

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x , y = x - 1, y - 1
    count[x][y] = 1

for _ in range(t):
    simulate(x, y, square)

answer = 0
for i in range(n):
    for j in range(n):
        answer += count[i][j]

print(answer)