n, t = list(map(int, input().split()))
r, c, d = input().split()
x, y = int(r) - 1, int(c) - 1

matrix, row = [], [0 for _ in range(n)]
for _ in range(n):
    matrix.append(row)

dirDict = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}
#      U  R  L  D
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0] 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dir_num = dirDict[d]
now = 0
while now < t:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny):
        now += 1
        dir_num = 3 - dir_num
        continue
    x, y = nx, ny
    now += 1
print(x+1, y+1)