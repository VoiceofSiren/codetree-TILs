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
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max_value(x, y, square):
    max_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value

def get_dir_num(x, y, square):
    dir_num = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] == get_max_value(x, y, square):
            dir_num = i
            break
    # print(f'(x, y) = ({x}, {y}) / dir_num = {dir_num}')
    return dir_num

def move(x, y, square):
    temp_value = temp_count[x][y]
    temp_count[x][y] = 0
    dir_num = get_dir_num(x, y, square)
    x = x + dx[dir_num]
    y = y + dy[dir_num]
    temp_count[x][y] += temp_value


rc_list = []
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    r, c = r - 1, c - 1
    rc_list.append([r, c])
    temp_count[r][c] = 1

for time in range(t):
    # print('==============================')
    # print(f'time = {time + 1}')
    # print('------------------------------')
    for i in range(m):
        x, y = rc_list[i][0], rc_list[i][1]
        move(x, y, square)

result = 0
for row in temp_count:
    for element in row:
        if element >= 1:
            result += 1
print(result)