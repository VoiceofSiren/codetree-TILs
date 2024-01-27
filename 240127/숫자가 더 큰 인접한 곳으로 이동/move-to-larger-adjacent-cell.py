n, r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
square = [list(map(int, input().split())) for _ in range(n)]

print(square[r][c], end=' ')

#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def compare():
    dir_num = -1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] > square[r][c]:
            dir_num = i
            break
    return dir_num

def move():
    global r, c
    dir_num = compare()

    if dir_num == -1:
        return False
    
    r = r + dx[dir_num]
    c = c + dy[dir_num]
    print(square[r][c], end=' ')
    return True

while True:
    m = move()
    if m == False:
        break