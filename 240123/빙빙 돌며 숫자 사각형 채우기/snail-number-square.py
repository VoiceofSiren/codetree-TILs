n, m = map(int, input().split())

square = [[ 0 for j in range(m)] for i in range(n)]
#     E  S  W  N
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
for i in range(1, n*m + 1):
    square[x][y] = i

    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if in_range(nx, ny) and square[nx][ny] == 0:
        x = nx
        y = ny
    else:
        dir_num = (dir_num + 1) % 4
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        x = nx
        y = ny

for i in range(n):
    for j in range(m):
        print(square[i][j], end=' ')
    print()